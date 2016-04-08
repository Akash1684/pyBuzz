# pyBuzz
A python script that sends weather forecast summary along with word of the day to your mobile phone

![](Screenshot.png)

Dependencies
---
* [Python 3](https://www.python.org/downloads/)
* forecastio (To install <code>pip install forecastio</code>)
* twilio (To install <code>pip install twilio</code>)
* Beautifulsoup (To install <code>pip install beautifulsoup4</code>)

Please note that this script requires an twilio account, you need to enter your assigned `sid` and `phone number` of your twilio account. (Signup [here](https://www.twilio.com))

Execution
---
A simple way is to directly execute [weather_buzz.py](https://github.com/Akash1684/pyBuzz/raw/master/weather_buzz.py)
<br><br>
You can also schedule the script to execute whenever you switch on your system (**Windows only**) to do this:
* Download and unzip the repository
* Open command prompt in the current directory
* Run `python setup.py py2exe`
* Two folder will be created *__pycache__* and *dist*.
* Copy the python compiled file present in *__pycache__*
* Paste it in the startup folder of the window

To do
---
* Adding subscription module that will allow multiple subscriber mobiles to recieve message simultaneously.

<br></br>
**Note**: To find longitude and latitude of your location [visit](http://www.latlong.net/)
  
