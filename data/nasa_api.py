#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# working with API NASA for geting info from asteroid's
# Reinan Br 08/12/2021 14:10
# 
# 
from datetime import datetime,timedelta
import requests as rq
import json
import time


#reading the .config.json for getting the key from API NASA#
with open('data/.config.json','r') as base_config:
    config = json.loads(base_config.read())

#config={ "key":"sXA0C4TYfSHFyRILNgknWnatwC9Wp823xXdjn7Fl"}
now = datetime.now()
now_init = now-timedelta(7)
date_time_init = now_init.strftime("%Y-%m-%d")
date_time_end = now.strftime('%Y-%m-%d')

def log(*args,name_file=False):
    res = []
    for txt in args:
        res.append(str(txt))
    res = ' '.join(res)
    date_time_debug = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(f'[{date_time_debug}] {res}')
    
    
path_file = 'log'
def log_save(*args):
    res = []
    for txt in args:
        res.append(str(txt))
    res = ' '.join(res)
    with open(path_file,'a') as file_log:
        file_log.write(res+'\n')
    print(res)

def api_nasa_asteroid(date_init=date_time_init,date_end=date_time_end):
    key=config['key']
    url_nasa_asteroid=f'https://api.nasa.gov/neo/rest/v1/feed?start_date={date_init}&end_date={date_end}&api_key={key}'
    time_init = time.time()
    data_nasa_asteroid = rq.get(url_nasa_asteroid).json()
    ping = (time.time()-time_init)
   
    print(f'[ping API NASA: {ping:.2f}s]')
    with open('data_asteroid.json','w') as data_asteroid:
        data_asteroid.write(json.dumps(data_nasa_asteroid))
    
    return (data_nasa_asteroid,ping)


#asteroids,ping = api_nasa_asteroid()['near_earth_objects']

path_file = 'asteroids_from_week.txt'

# log_save(10*'=+=','asteroids from week',10*'=+=')
# for _key_ in list(asteroids.keys()):
#     log_save('')
#     log_save()
#     log_save(5*'=+=',f'asteroids from day {_key_}',5*'=+=')
#     #log_save(f'[day: {_key_}]')
#     for asteroid in asteroids[_key_]:
#         name = asteroid["name"]
#         speed = float(asteroid["close_approach_data"][0]["relative_velocity"]["kilometers_per_second"])

#         diameter_min = float(asteroid["estimated_diameter"]["meters"]["estimated_diameter_min"])
#         diameter_max = float(asteroid["estimated_diameter"]["meters"]["estimated_diameter_max"])
#         diameter = (diameter_max+diameter_min)/2
        
#         dist = float(asteroid["close_approach_data"][0]["miss_distance"]["lunar"])
#         mag = float(asteroid["absolute_magnitude_h"])

#         log_save('')
#         log_save(3*'=+=',f'name: {name}',3*'=+=')
#         log_save(f"speed: {speed:.2f} km/s")
#         log_save(f"diameter: {diameter:.2f} m")
#         log_save(f"distance: {dist:.2f} lunar")
#         log_save(f"magnetude: {mag}")
        
        