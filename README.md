Weather report box - WiPy 2.0, Ublox NEO-6M, ST7735 Display
------------------------------------------------
This project is about connecting a Wipy 2.0 with and Ublox NEO-6M GPS and a ST7735 display. The Wipy 2.0 gets the GPS coordinates, makes a get request to obtain weather information and displays this info on the LCD.

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
<iframe src="https://www.youtube.com/embed/F7brePK7bYE?controls=1" width="80%" height="300" allowfullscreen=""></iframe>

Changelog
-------------------
* Revision 0.1b

More Info:
-----------
* Blog article: http://lemariva.com/blog/2017/01/wipy-2-0-weather-report

Credits
--------------------
* GPS library forked from: https://github.com/inmcm/micropyGPS
* ST7735 library rewriten from: http://forum.43oh.com/topic/4352-universal-color-lcd-graphics-library-2/

License:
---------------
* MIT, Apache 2.0 (check files)
