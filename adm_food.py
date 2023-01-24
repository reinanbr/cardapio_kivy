
import firebase_admin
from firebase_admin import credentials,firestore
import datetime
import time
# from firebase_admin import db
import json


cred = credentials.Certificate("keys/fire_key.json")
app = firebase_admin.initialize_app(cred)


db = firestore.client()


# add food
def add_food(food):
    try:
        foods = db.collection('foods')

        food_json = {
            "name":food,
            "like":0,
            "dislike":0,
            "date_update":str(datetime.datetime.now()),
            "time_update":time.time(),
            "usersLikeList":[],
            "usersDislikeList":[]
        }
        foods.document(food).set(food_json)
        return True,food_json
    except:
        return False


# read food
def get_food_day():

    foods = db.collection('foods')
    get_foods = foods.stream()
    foods_list = []

    for fds in get_foods:
        fds = fds.to_dict()
        foods_list.append(fds)


    food_day = foods_list[0]
    for fd in foods_list:
        if fd['time_update']>food_day['time_update']:
            food_day = fd
        # else:
        #     food_day = fds

    return food_day


#function for like
def like(food,user):
    #food['like'] = food['like']+1
    user_key = user['userKey']
    if not (user_key in food['usersLikeList']):
        food['usersLikeList'].append(user_key)
    else:
        pass
    
    if user_key in food['usersDislikeList']:
        food['usersDislikeList'].remove(user_key)
        
    food['like'] = len(food['usersLikeList']) - 1 if len(food['usersLikeList'])>0 else 0

    food['dislike'] = len(food['usersDislikeList']) - 1 if len(food['usersDislikeList'])>0 else 0

    foods = db.collection('foods')
    foods.document(food['name']).set(food)



#function for dislike
def dislike(food,user):
    user_key = user['userKey']
    if not (user_key in food['usersDislikeList']):
        food['usersDislikeList'].append(user_key)
    else:
        pass
    
    if user_key in food['usersLikeList']:
        food['usersLikeList'].remove(user_key)
        
    food['like'] = len(food['usersLikeList']) - 1 if len(food['usersLikeList'])>0 else 0

    food['dislike'] = len(food['usersDislikeList']) - 1 if len(food['usersDislikeList'])>0 else 0

    foods = db.collection('foods')
    foods.document(food['name']).set(food)



# #read
# data = db.collection('users').stream()

# for user in data:
#     usr = user.to_dict()
#     print(usr)
# # users = db.collection('users')

# # users.document('user1').set(
#     {"ip":"127.0.0.1",
#      "UserAgent":"linux",
#      "date":"N"}
#     )