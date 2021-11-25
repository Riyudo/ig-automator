class User():
    "To better hold data of instagram users"
    def __init__(self, user_list):
        self.pk = user_list[0]
        self.username = user_list[1]
        self.is_private = user_list[2]
        self.follower_count = user_list[3]
        self.following_count = user_list[4]

    def get_ratio(self):
        if (self.following_count > 0):
            return self.follower_count/self.following_count
        return 0

    def print_userinfo(self):
        print(self.pk)
        print(self.username)
        print(self.is_private)
        print(self.follower_count)
        print(self.following_count)

