import functions
import sys
import os
from datetime import date
from datetime import datetime

dir1 = os.getcwd()
if ("/home/masuday" in dir1):
    sys.path.append('/home/masuday/tools/py-env3')

import mysql.connector as mydb
from bs4 import BeautifulSoup
import pandas as pd
import requests

conn = mydb.connect(host='localhost', user='masuday_tools',
                    password='Kurodai', database='masuday_tools')
curs = conn.cursor()
sql_code = "INSERT IGNORE INTO wea_observation (observ_date, point_name, point_no, air_press, sl_press, ave_temp, max_temp, min_temp, "
sql_code += "ave_humidity, min_humidity, ave_wind, max_wind, max_direction, mom_wind, mom_direction, sunshine, total_rain, hour_rain, "
sql_code += "10min_rain, snow, snow_height, 1st_desc, 2nd_desc) VALUES ('%s', '%s', %d, %f, %f, %f, %f, %f, %f, %f, %f, %f, '%s', %f, '%s', %f, %f, %f, %f ,%f, %f, '%s', '%s')"

url = "https://www.data.jma.go.jp/obd/stats/data/mdrr/synopday/data2.html"
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')
soup = soup.find('div', style='margin-top:5px; text-align:center')
observ_date = soup.text[-12:-2].replace("年", "-").replace("月", "-")
dfw = pd.read_html(url, header=2)
for x in range(5):
    dfw[x].columns = ['point_name', 'air_press', 'sl_press', 'ave_temp', 'max_temp', 'min_temp', 'ave_humidity', 'min_humidity', 'ave_wind', 'max_wind',
                      'max_direction', 'mom_wind', "mom_direction", "sunshine", "total_rain", "hour_rain", "10min_rain", "snow", "snow_height", "1st_desc", "2nd_desc"]
    for i in range(len(dfw[x].index)):
        point_no = functions.get_intlNo(dfw[x].loc[i]["point_name"])
        point_name = dfw[x].loc[i]["point_name"]
        air_press = functions.check_float(dfw[x].loc[i]["air_press"])
        sl_press = functions.check_float(dfw[x].loc[i]["sl_press"])
        ave_temp = functions.check_float(dfw[x].loc[i]["ave_temp"])
        max_temp = functions.check_float(dfw[x].loc[i]["max_temp"])
        min_temp = functions.check_float(dfw[x].loc[i]["min_temp"])
        ave_humidity = functions.check_float(dfw[x].loc[i]["ave_humidity"])
        min_humidity = functions.check_float(dfw[x].loc[i]["min_humidity"])
        ave_wind = functions.check_float(dfw[x].loc[i]["ave_wind"])
        max_wind = functions.check_float(dfw[x].loc[i]["max_wind"])
        max_direction = functions.check_string(dfw[x].loc[i]["max_direction"])
        mom_wind = functions.check_float(dfw[x].loc[i]["mom_wind"])
        mom_direction = functions.check_string(dfw[x].loc[i]["mom_direction"])
        sunshine = functions.check_float(dfw[x].loc[i]["sunshine"])
        total_rain = functions.check_float(dfw[x].loc[i]["total_rain"])
        hour_rain = functions.check_float(dfw[x].loc[i]["hour_rain"])
        ten_min_rain = functions.check_float(dfw[x].loc[i]["10min_rain"])
        snow = functions.check_float(dfw[x].loc[i]["snow"])
        snow_height = functions.check_float(dfw[x].loc[i]["snow_height"])
        first_desc = functions.check_string(dfw[x].loc[i]["1st_desc"])
        second_desc = functions.check_string(dfw[x].loc[i]["2nd_desc"])
        # print(sql_code %(observ_date, point_name, point_no, air_press, sl_press, ave_temp, max_temp, min_temp, ave_humidity, min_humidity, ave_wind, \
        #     max_wind, max_direction, mom_wind, mom_direction, sunshine, total_rain, hour_rain, ten_min_rain, snow, snow_height, first_desc, second_desc))
        curs.execute(sql_code %(observ_date, point_name, point_no, air_press, sl_press, ave_temp, max_temp, min_temp, ave_humidity, min_humidity, ave_wind, \
            max_wind, max_direction, mom_wind, mom_direction, sunshine, total_rain, hour_rain, ten_min_rain, snow, snow_height, first_desc, second_desc))
        conn.commit()

curs.close()
conn.close()
