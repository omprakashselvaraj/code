from logging import debug
import requests
from flask import Flask, jsonify, request
#from flask_restful import Resource, Api
from urllib.request import urlretrieve
from pprint import PrettyPrinter, pprint

app = Flask(__name__)


pp = PrettyPrinter()

apiKey = 'TidP7NUQAdecvBjagQBF1bC6PMPsETyV8BCDFPQm'


#--------------------------------------SECTION 1----------------------------------
@app.route('/nasa/image-of-month',methods=['GET'])
def task():
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

@app.route('/nasa/image-of-month/<year>/<month>',methods=['GET'])
def task1(year,month):
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


@app.route('/nasa/videos-of-month/<year>/<month>',methods=['GET'])
def task2(year,month):
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

@app.route('/nasa/earth-poly-image/<date>',methods=['GET'])
def task3(date):
  URL_APOD = "https://epic.gsfc.nasa.gov/api/images.php"
  sdate = date
  try:
    params = {
        'api_key':apiKey,
        'date':sdate,
    }
    response = requests.get(URL_APOD,params=params).json()
    li=[]
    for i in response:
          a=int(i['centroid_coordinates']['lat'])
          b=int(i['centroid_coordinates']['lon'])
          if a in range(10,40) and b in range(120,161):
            dic={'identifier':i['identifier'],'caption':i['caption'],'image':i['image'],'date':i['date'],'latitude':i['centroid_coordinates']['lat'],'longitude':i['centroid_coordinates']['lon']}
            li.append(dic)
    return str(li)
  except:
    js={"status": 404,"message": "image/video not found"}
    return js

#-------------------------------------------section 2-----------------------------------------

@app.route('/weather/city/<name>',methods=['GET'])
def task4(name):
  try:
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    API_KEY = "fb725cc2dc004d6ab823186d2c27fab1"
    # upadting the URL
    URL_APOD = BASE_URL + "q=" + name + "&units=metric&appid=" + API_KEY
    # HTTP request
    response = requests.get(URL_APOD).json()
    #pp.pprint(response)
    dic={'country':response['sys']['country'],'name':response['name'],'temp':response['main']['temp']}
    return dic
  except:
    js={
    "status": 404,
    "message": "weather data not found"
    }
    return js


@app.route('/weather/search/',methods=['GET'])
def task5():
  temp={}
  API_KEY="fb725cc2dc004d6ab823186d2c27fab1"
  try:
        q_Param=str(request.query_string)[2:]        
        if(q_Param[0]=='p'):
            key,val=map(str,q_Param.split('='))
            val=val[:-1]            
            response=requests.get("https://api.openweathermap.org/data/2.5/weather?zip="+val+",in&units=metric&appid="+API_KEY)        
        else:
            lat,lon=map(str,q_Param.split('&'))
            latV=lat.split('=')[1]
            lonV=lon.split('=')[1]
            lonV=lonV[:-1]
            response=requests.get("https://api.openweathermap.org/data/2.5/weather?lat="+latV+"&lon="+lonV+"&units=metric&appid="+API_KEY)        
        response=response.json()      
        temp['country']= response["sys"]["country"]
        temp['name']=response["name"]
        temp['temp']=response["main"]["temp"]
        temp['min_temp']=response["main"]["temp_min"]
        temp['max_temp']=response["main"]["temp_max"]
        temp['latitude']=response["coord"]["lat"]
        temp['longitude']=response["coord"]["lon"]
        dic={"country":temp['country'],"name":temp['name'],"temp":temp['temp'],"min_temp":temp['min_temp'],"max_temp":temp['max_temp'],"latitude":temp['latitude'],"longitude":temp['longitude']}
        return dic
  except:
        js={"status": 404,"message": "weather data not found"}
        return js

@app.route('/',methods=['GET'])
def start():
  js={"data":"codeCrunch21 -> 06-oct-21"}
  return js

if __name__=='__main__':
  app.run(debug=True)