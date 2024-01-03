import json
    
def get_intlNo(point_name):
  return_val=99999
  dump = open('/home/masuday/domains/wsmeguro.jp/scripts/weather2/ctf/points_observe.json', 'r')
  points = json.load(dump)
  for point in points:
    if (point_name in point['PointName']):
      return_val=int(point['IntlNo'])
  return return_val

def check_int(hp_data):
    try:
        ret_value=int(hp_data)
    except:
        ret_value=0
    return ret_value

def check_float(hp_data):
    try:
        ret_value=float(hp_data)
    except:
        ret_value=0.0
    if str(ret_value)=='nan':
        ret_value=0.0
    return ret_value

def check_string(hp_data):
    try:
        ret_value=str(hp_data)
    except:
        ret_value="--"
    return ret_value