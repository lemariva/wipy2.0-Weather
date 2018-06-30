Weather report box - WiPy 2.0, Ublox NEO-6M, ST7735 Display
------------------------------------------------
This project is about connecting a Wipy 2.0 with an Ublox NEO-6M GPS and a ST7735 display. The Wipy 2.0 gets the GPS coordinates, makes a get request to obtain weather information (using the Open Weather Map API) and displays this info on the LCD.

Hardware
----------------
* Wipy 2.0
* Ublox NEO-6M or NEO-M8N
* ST7735 display

Check the blog article for more information:  http://lemariva.com/blog/2017/01/wipy-2-0-weather-report-box

Wiring 
---------------

|		|		|		|
|:-----:|:-----:|:-----:|
|**Wipy 2.0**|**NEO-6M**|**ST7735**|
| `3.3v`| `VCC` | `VCC`|
| `GND` | `GND` | `GND`|
| `P3`(`G12`) | `RX`  |	   |
| `P4`(`G11`) | `TX`  |	   |
| `P6`(`G13`) |   |	 `RES`  |
| `P7`(`G14`) |   |	 `RS/DC`  |
| `P8`(`G15`) |   |	 `CS`  |
| `P10`(`G17`) |   |	 `SCL`  |
| `P11`(`G22`) |   |	 `SDA`  |

Preview
--------------------
[![wipy2.0-Weather](https://img.youtube.com/vi/F7brePK7bYE/0.jpg)](https://www.youtube.com/watch?v=F7brePK7bYE)

Changelog
-------------------
* Revision 0.1b

More Info:
-----------
* Blog article: http://lemariva.com/blog/2017/01/wipy-2-0-weather-report-box

Credits
--------------------
* GPS library forked from: https://github.com/inmcm/micropyGPS
* ST7735 library rewriten from: http://forum.43oh.com/topic/4352-universal-color-lcd-graphics-library-2/

License:
---------------
* MIT, Apache 2.0 (check files)
