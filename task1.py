from logging import debug
import requests
from flask import Flask, jsonify, request
#from flask_restful import Resource, Api
from urllib.request import urlretrieve
from pprint import PrettyPrinter, pprint

app = Flask(__name__)


pp = PrettyPrinter()

apiKey = 'TidP7NUQAdecvBjagQBF1bC6PMPsETyV8BCDFPQm'
@app.route('/nasa/image-of-month',methods=['GET','POST'])
def fetchAPOD():
  URL_APOD = "https://api.nasa.gov/planetary/apod"
  date = '2021-10-01'
  try:
    params = {
        'api_key':apiKey,
        'date':date,
    }
    response = requests.get(URL_APOD,params=params).json()
    dict={'date':response['date'],'media_type':response['media_type'],'title':response['title'],'url':response['url']}
    pp.pprint(response)
    return dict
  except:
    js={"status": 404,"message": "image/video not found"}
    return js

@app.route('/nasa/image-of-month/<year>/<month>')
def fetchAPOD1(year,month):
  URL_APOD = "https://api.nasa.gov/planetary/apod"
  c=0
  day=0
  y=int(year)
  m=month
  s1={'January','March','May','July','August','October','December'}
  s2={'April','June','September','November'}
  if((y % 400 == 0) or  (y % 100 != 0) and  (y % 4 == 0)):
    c=1
  if c==1 and m=="February":
    day=29
  elif c==0 and m=="February":
    day=28
  else:
    if m in s1:
      day=31
    else:
      day=30
  di={'January':"01",'February':"02",'March':"03",'April':"04",'May':"05",'June':"06",
      'July':'07','August':"08",'September':"09",'October':"10",'November':"11",'December':"12"
      }
  mo=di[m]
  sdate=str(y)+"-"+mo+"-"+"01"
  edate=str(y)+"-"+mo+"-"+str(day)
  try:
    params = {
        'api_key':apiKey,
        'start_date':sdate,
        'end_date':edate,
    }
    response = requests.get(URL_APOD,params=params).json()
    li=[]
    #dict={'date':response['date'],'media_type':response['media_type'],'title':response['title'],'url':response['url']}
    for i in response:
        li.append(i['url'])
    return str(li)
  except:
    js={"status": 404,"message": "image/video not found"}
    return js


@app.route('/nasa/videos-of-month/<year>/<month>')
def fetchAPOD2(year,month):
  URL_APOD = "https://api.nasa.gov/planetary/apod"
  c=0
  day=0
  y=int(year)
  m=month
  s1={'January','March','May','July','August','October','December'}
  s2={'April','June','September','November'}
  if((y % 400 == 0) or  (y % 100 != 0) and  (y % 4 == 0)):
    c=1
  if c==1 and m=="February":
    day=29
  elif c==0 and m=="February":
    day=28
  else:
    if m in s1:
      day=31
    else:
      day=30
  di={'January':"01",'February':"02",'March':"03",'April':"04",'May':"05",'June':"06",
      'July':'07','August':"08",'September':"09",'October':"10",'November':"11",'December':"12"
      }
  mo=di[m]
  sdate=str(y)+"-"+mo+"-"+"01"
  edate=str(y)+"-"+mo+"-"+str(day)
  try:
    params = {
        'api_key':apiKey,
        'start_date':sdate,
        'end_date':edate,
        'thumbs':True,
    }
    response = requests.get(URL_APOD,params=params).json()
    li=[]
    
    for i in response:
        if i['media_type']=='video':
          li.append(i['url'])
    return str(li)
  except:
    js={"status": 404,"message": "image/video not found"}
    return js


if __name__=='__main__':
  app.run(debug=True)



