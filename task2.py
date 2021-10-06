import requests
from urllib.request import urlretrieve
from pprint import PrettyPrinter, pprint


pp = PrettyPrinter()

apiKey = 'TidP7NUQAdecvBjagQBF1bC6PMPsETyV8BCDFPQm'

def fetchAPOD():
  URL_APOD = "https://epic.gsfc.nasa.gov/api/natural"
  sdate = '2019-04-15'
  #edate = '2020-05-31'
  params = {
      'api_key':apiKey,
      'date':sdate,
      #'end_date':edate,
      #'thumbs':True,
  }
  response = requests.get(URL_APOD,params=params).json()
  #pp.pprint(response)
  li=[]
 
  for i in response:
        a=i['centroid_coordinates']['lat']
        b=i['centroid_coordinates']['lon']
        print(a,b)
        #if a in range(100,141) and b in range(120,161):
          #li.append(a)
  print(li)
fetchAPOD()