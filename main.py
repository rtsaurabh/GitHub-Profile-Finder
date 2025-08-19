import requests
import pandas

username = input("Type the username about which you want info: ")

user_res = requests.get(f"https://api.github.com/users/{username}")

data = user_res.json()



try:
    user_data ={"Data Type":["Name","Company","Followers","Following","Public Repos","Public Gists"],
       "Data":[data["name"],data["company"],data["followers"],data["following"],data["public_repos"],data["public_gists"]]}
    user = pandas.DataFrame(user_data)

    print(user.to_string(index=False))

except KeyError as message:
    message = "User not found."
    print(message)







# print(user_data)

# print(data)