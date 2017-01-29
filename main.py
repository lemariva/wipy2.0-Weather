#Copyright [2017] [Mauro Riva <lemariva@mail.com> <lemariva.com>]

#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at

#http://www.apache.org/licenses/LICENSE-2.0

#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.

#The above copyright notice and this permission notice shall be
#included in all copies or substantial portions of the Software.  

from machine import UART, Pin
from graphics import Display
from ublox_gps import MicropyGPS
from fonts import font_6x8
import http_client
import time, utime

def initDisplay():
    # display 
    my_display.clearScreen()    
    my_display.drawString(10,10,'LeMaRiva', font_6x8, my_display.COLOR_RED, 2)    
    my_display.drawString(10,30,'City:', font_6x8, my_display.COLOR_GREEN, 1)
    my_display.drawString(10,40,'Country:', font_6x8, my_display.COLOR_GREEN, 1)
    my_display.drawString(10,50,'Temp:', font_6x8, my_display.COLOR_GREEN, 1)
    my_display.drawString(10,60,'Pressure:', font_6x8, my_display.COLOR_GREEN, 1)
    my_display.drawString(10,70,'Humidity:', font_6x8, my_display.COLOR_GREEN, 1)
    my_display.drawString(10,80,'Weather:', font_6x8, my_display.COLOR_GREEN, 1)            


def updatingWeather(stat, my_gps, my_display):    
    
    WEBADDRESS = 'http://api.openweathermap.org/data/2.5/weather?lat=$LATITUDE$&lon=$LONGITUDE$&units=metric&appid='
    API = '######API KEY HERE######'
    
    if(stat != None):
        # changing gps coodinates to get the weather status
        address = WEBADDRESS + API
        address = address.replace('$LATITUDE$', str(my_gps.latitude_decimal()))
        address = address.replace('$LONGITUDE$', str(my_gps.longitude_decimal()))
        try:
            # get request
            r = http_client.get(address)
            r.raise_for_status()
            
            # processing get request
            if (r.status_code == 200):                    
                weather_data = r.json()            
                sys = weather_data['sys']            
                weather_condition = weather_data['weather']
                weather_condition = weather_condition[0]
                weather_main = weather_data['main']
                # city
                my_display.drawString(50,30, weather_data['name'], font_6x8, my_display.COLOR_WHITE, 1)
                # country
                my_display.drawString(65,40,sys['country'], font_6x8, my_display.COLOR_WHITE, 1)
                # temp
                my_display.drawString(50,50,str(weather_main['temp']) + ' C', font_6x8, my_display.COLOR_WHITE, 1)
                # pressure
                my_display.drawString(75,60,str(weather_main['pressure']), font_6x8, my_display.COLOR_WHITE, 1)            
                # humidity
                my_display.drawString(75,70,str(weather_main['humidity']), font_6x8, my_display.COLOR_WHITE, 1)                        
                # weather
                my_display.drawString(70,80, weather_condition['main'], font_6x8, my_display.COLOR_WHITE, 1)                                    
                my_display.drawString(20,90, weather_condition['description'], font_6x8, my_display.COLOR_WHITE, 1)         
                
                # update status
                my_display.drawCircle(149, 117, 10,  my_display.COLOR_GREEN)
            else:
                # update status
                my_display.drawCircle(149, 117, 10,  my_display.COLOR_RED)    
        except:     # website problems
            pycom.rgbled(0x220000) 
            my_display.drawCircle(149, 117, 10,  my_display.COLOR_RED)    
            my_gps.stringclean()        
            time.sleep_ms(2000)     


# Update rates in ms    
UPDATE_GPS = const(10000)
UPDATE_WEATHER = const(50000)
    
pycom.rgbled(0x000011)  # hearbeat

# GPS initialization
uart = UART(1, 9600)                          # init with given baudrate
uart.init(9600, bits=8, parity=None, stop=1)  # init with given parameters

my_gps = MicropyGPS()

# DISPLAY initialization
my_display = Display()
my_display.clearScreen() # ClearScreen

# VARIABLE initialization
stat = None

# Update times
updateWeather = utime.ticks_ms()
updateGPS = utime.ticks_ms()

while True:        
    try:
        pycom.rgbled(0x000500)  # hearbeat
        
        # Updating GPS position
        if(utime.ticks_ms() - updateGPS >= UPDATE_GPS):
            updateGPS = utime.ticks_ms()
            stat = my_gps.updateall(uart.readall())            
                
        # Reporting GPS Status
        if(stat != None):
            my_display.drawCircle(149, 117, 5,  my_display.COLOR_GREEN)
        else:
            # update status
            my_display.drawCircle(149, 117, 5,  my_display.COLOR_RED)            

        # Updating weather condition
        if(utime.ticks_ms() - updateWeather >= UPDATE_WEATHER):
            updateWeather = utime.ticks_ms()
            initDisplay()
            updatingWeather(stat, my_gps, my_display)
                        
        # hearbeat
        time.sleep_ms(1000)
        pycom.rgbled(0x050505)         
        time.sleep_ms(1000)                            
        
    except:     # gps problems
        pycom.rgbled(0x220000) 
        my_display.drawCircle(149, 117, 5,  my_display.COLOR_RED)           
        my_gps.stringclean()        
        time.sleep_ms(2000)     
