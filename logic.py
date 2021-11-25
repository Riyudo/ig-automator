from instagram_private_api import Client, ClientCompatPatch


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
            
        #print(user_info[attribute])


    def get_pk(self, username):
        "Receives pk from user"
        info = self.api.username_info(username) #HARDCODED
        print(info)


    def options(self):
        print("Options: ")

    def welcome(self):
        print("Welcome " + self.user_name)