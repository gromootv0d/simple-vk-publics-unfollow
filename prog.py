import vk
import time

print("to get acces tocken go to url: https://oauth.vk.com/authorize?client_id=7471466&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=wall,groups&response_type=token")
access_token = 'token add here'

session = vk.Session(access_token=access_token)
print(session)
v = '5.103'
api = vk.API(session=session, v=v, scope='wall')

wall = api.groups.get()
print(wall['items'])
for i in wall['items']:
    api.groups.leave(group_id=168074096)
    time.sleep(0.3)

 
