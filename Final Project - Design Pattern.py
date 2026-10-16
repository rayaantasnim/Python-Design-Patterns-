# ==============================================================================
# 📱 INSTAGRAM NOTIFICATION SYSTEM SIMULATION
# ==============================================================================
# Description: A Python implementation of the behavioral Observer Design Pattern.
# Component  : Demonstrates low-coupling publisher (Subject) and subscriber (Observer) mechanics.
# Features   : Multi-channel support with dynamic follower subscription and real-time updates.
# ==============================================================================



# ========================================================
# 📢 1. Subject or Publisher Class (Instagram User/Channel)
# ========================================================
class InstagramUser:
    def __init__(self, username):
        self.name = username
        self._followers = []  # List to store observers (followers)
        self._latest_post = None

    # Method to follow
    def follow(self, follower):
        if follower not in self._followers:
            self._followers.append(follower)

    # Method to unfollow (Fixed to prevent ValueError)
    def unfollow(self, follower):
        if follower in self._followers:
            self._followers.remove(follower)

    # Notify all followers when a new post is uploaded
    def notify_followers(self):
        for follower in self._followers:
            # Added a safety check to ensure the follower object is valid
            if follower is not None:
                follower.update(self.name, self._latest_post)

    # Main logic for uploading a post
    def upload_post(self, post_title):
        self._latest_post = post_title
        print(f"\n🚀 [{self.name}] uploaded a new post: '{post_title}'")
        self.notify_followers()  # Automatically notify everyone!


# ========================================================
# 👥 2. Observer or Subscriber Class (Follower)
# ========================================================
class Follower:
    def __init__(self, user_name):
        self.name = user_name

    # Method to receive updates
    def update(self, creator_name, post_title):
        print(f"  🔔 {self.name} received a notification: {creator_name} posted '{post_title}'")


# ========================================================
# ⚙️ --- Usage (Client Code) ---
# ========================================================

print("✨ --- Welcome to the Instagram Notification System --- ✨")

# ---------------------------------------------
# 🌐 CHANNEL 1: Web Development
# ---------------------------------------------
web_dev_channel = InstagramUser("Web Dev Tips 🌐")

user1 = Follower("Karim")
user2 = Follower("Sakib")
user3 = Follower("Nabila")
user4 = Follower("Arif")
user5 = Follower("Tahsin")

web_dev_channel.follow(user1)
web_dev_channel.follow(user2)
web_dev_channel.follow(user3)
web_dev_channel.follow(user4)
web_dev_channel.follow(user5)

web_dev_channel.upload_post("Learn Flexbox in 5 Minutes!")


# ---------------------------------------------
# 💻 CHANNEL 2: Programming
# ---------------------------------------------
programming_channel = InstagramUser("Programming Zone 💻")

user6 = Follower("Rahim")
user7 = Follower("Fahim")
user8 = Follower("Sadia")
user9 = Follower("Zayan")
user10 = Follower("Mitu")

programming_channel.follow(user6)
programming_channel.follow(user7)
programming_channel.follow(user8)
programming_channel.follow(user9) # FIXED: Removed the nested method call
programming_channel.follow(user10)

programming_channel.upload_post("Introduction to Python Objects!")


# ---------------------------------------------
# 🗄️ CHANNEL 3: Database Systems
# ---------------------------------------------
database_channel = InstagramUser("Database Hub 🗄️")

user11 = Follower("Imran")
user12 = Follower("Riya")
user13 = Follower("Tanvir")
user14 = Follower("Anika")
user15 = Follower("Siam")

database_channel.follow(user11)
database_channel.follow(user12)
database_channel.follow(user13)
database_channel.follow(user14)
database_channel.follow(user15)

database_channel.upload_post("SQL vs NoSQL: Which one to choose?")

print("\n🎉 --- Notification Simulation Finished Successfully! --- 🎉")
