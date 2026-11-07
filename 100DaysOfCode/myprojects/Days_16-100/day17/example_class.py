class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

    def unfollow(self, user):
        user.followers -= 1
        self.following -= 1

    def print_following(self):
        print(
            f"Username: {self.username} | "
            f"Followers: {self.followers} | "
            f"Following: {self.following}"
        )


user1 = User("001", "Pierre")
user2 = User("002", "Luis")

user1.follow(user2)
user1.print_following()
user2.print_following()

