import forecastio
from twilio.rest import TwilioRestClient
from bs4 import BeautifulSoup
import urllib.request

def scrap():
    r = urllib.request.urlopen('https://www.randomlists.com/random-vocabulary-words') #open the webpage for scraping
    soup = BeautifulSoup(r,"html.parser")
    word = 'WORD OF THE DAY' + ' : ' + soup.find('span',{'class':'support'}).text.title() + '- ' + soup.find('span',{'class':'subtle'}).text
    return word

#DETAILS: https://github.com/ZeevG/python-forecast.io
def forcast_handle(lat,lng):                           
    api_key = "8d8761e72fd4aa397a8c54c6f1c256c6"   
    forecast = forecastio.load_forecast(api_key, lat, lng)
    byHour = forecast.hourly()
    return "WEATHER FORECAST: " + byHour.summary

def textmyself(message):
    sid = "AC2943bced271470a0b31a328d7266bba0"
    token = "34845e7364b55d067fe4b00c75d7585f"
    myNumber = "+919454028991"
    twilioNumber = "+12318034148"
    twilioClient=TwilioRestClient(sid,token)
    twilioClient.messages.create(body=message,from_=twilioNumber,to=myNumber)

def main():
    forcast= forcast_handle(25.594095,85.137565)
    scrap_data= scrap()
    msg = forcast + '\n\n' + scrap_data
    textmyself(msg)  #send message to mobile
    #print(msg)


if __name__ == "__main__": main()
