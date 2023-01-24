from pathlib import Path
import secrets
import json
import os

#key = secrets.token_urlsafe(16)

file_key = 'user_key.json'




#function for read options from it device
def save_user_opt(data) -> None:
    if os.path.isfile(file_key):
        with open(file_key,'r') as file:
            user_data = json.load(file)

        user_data['like'] = data['like']
        user_data['dislike'] = data['dislike']
        user_data['likeCount'] = user_data['likeCount'] + 1 if data['like'] else user_data['likeCount']
        user_data['dislikeCount'] = user_data['dislikeCount'] + 1 if data['dislike'] else user_data['dislikeCount']
        

        with open(file_key,'w') as file:
            json.dump(user_data,file)

    else:
         key_user = secrets.token_urlsafe(16)
         user = {"userKey":key_user,
                "food":'sem informações',
                "like":None,
                "dislike":None,
                "likeCount":0,
                "dislikeCount":0}
         with open(file_key,'w') as file:
            json.dump(user,file)

         save_user_opt(data)



#function for read options from it device
def read_user_opt():
    if os.path.isfile(file_key):
        with open(file_key,'r') as file:
            data_user = json.load(file)
        return data_user
    else:
         key_user = secrets.token_urlsafe(16)
         user = {"userKey":key_user,
                "food":'sem informações',
                "like":None,
                "dislike":None,
                "likeCount":0,
                "dislikeCount":0}
         with open(file_key,'w') as file:
            json.dump(user,file)

         return user



