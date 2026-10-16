# 1. Subject or Publisher Class (YouTube Channel)
class YouTubeChannel:
    def __init__(self, channel_name):
        self.name = channel_name
        self._subscribers = []  # List of observers
        self._latest_video = None

    # Method to subscribe
    def subscribe(self, subscriber):
        if subscriber not in self._subscribers:
            self._subscribers.append(subscriber)

    # Method to unsubscribe
    def unsubscribe(self, subscriber):
        self._subscribers.remove(subscriber)

    # Notify all subscribers when a new video is uploaded
    def notify_subscribers(self):
        for subscriber in self._subscribers:
            subscriber.update(self.name, self._latest_video)

    # Main logic for uploading a video
    def upload_video(self, video_title):
        self._latest_video = video_title
        print(f"\n[{self.name}] channel uploaded a new video: '{video_title}'")
        self.notify_subscribers()  # Automatically notify everyone
        

# 2. Observer or Subscriber Class
class Subscriber:
    def __init__(self, user_name):
        self.name = user_name

    # Method to receive updates
    def update(self, channel_name, video_title):
        print(f"-> {self.name} received notification: {channel_name} uploaded '{video_title}'")


# --- Usage (Client Code) ---

# Create a channel
my_channel = YouTubeChannel("CodeWithPython")

# Create some users/subscribers
user1 = Subscriber("Rahim")
user2 = Subscriber("Arif")
user3 = Subscriber("Tahsin")

# Subscribe them to the channel
my_channel.subscribe(user1)
my_channel.subscribe(user2)
my_channel.subscribe(user3)

# First video upload (all 3 will get notifications)
my_channel.upload_video("Learn Python Easily")

# Arif unsubscribes from the channel
my_channel.unsubscribe(user2)

# Second video upload (only Rahim and Tahsin will get notifications)
my_channel.upload_video("What is a Design Pattern?")
