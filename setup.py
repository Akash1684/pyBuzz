#setup.py

from distutils.core import setup
import py2exe

setup(
    console=['weather_buzz.py'],
    options= {
        'py2exe': {
            'packages' : ['forecastio', 'twilio.rest', 'bs4', 'urllib']
        }
    }
)