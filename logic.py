from instagram_private_api import Client, ClientCompatPatch
from user import User

class Logic():
    def __init__(self):
        credentials = input("Credentials: ").split(" ")
        self.user_name = credentials[0]
        self.password = credentials[1]
        self.api = Client(self.user_name, self.password)
        self.welcome()
    
    def clientInfo(self):
        user_info = self.api.username_info(self.user_name)["user"]
        print(user_info)
        user_info_separated = []
        for attribute in user_info:
            user_info_separated.append(attribute)
            print(attribute) 
            
        print(user_info[attribute])


    def get_pk(self, username):
        "Receives pk from user"
        info = self.api.username_info(username)["user"]
        #print(info['pk'])

    def get_userinfo(self, username):
        info = self.api.username_info(username)["user"]
        info_list = []
        info_list.append(info['pk'])
        info_list.append(info['username'])
        info_list.append(info['is_private'])
        info_list.append(info['follower_count'])
        info_list.append(info['following_count'])
        return info_list

    def create_user(self, info_list):
        user = User(info_list)
        return user

    def options(self):
        print("Options: ")

    def welcome(self):
        print("Welcome " + self.user_name)