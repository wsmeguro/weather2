import requests, json

urls = ["https://www.jma.go.jp/bosai/forecast/data/overview_forecast/",
        "https://www.jma.go.jp/bosai/forecast/data/forecast/"]

dump = open('/home/masuday/domains/wsmeguro.jp/scripts/weather2/ctf/points_forecast.json', 'r')
points = json.load(dump)
for point in points:
  for url in urls:
    info=url.replace("https://www.jma.go.jp/bosai/forecast/data/","")[:8]
    response = requests.get(url + point["code"] +  ".json")
    if response.status_code==200:
      file = open("/home/masuday/domains/wsmeguro.jp/public_html/weather/data/" + point["code"] + "_" + info + ".json","wb")
      for chunk in response.iter_content(100000):
        file.write(chunk)
      
      file.close()