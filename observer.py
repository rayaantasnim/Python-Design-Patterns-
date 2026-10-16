# -------------------------------
# Observer Pattern Example in Python
# -------------------------------
# Subject (Publisher): YouTube-Channel
# Observers (Subscribers): Subscriber
# Intent: When the subject changes state (uploads a video),
# all observers are automatically notified.
# -------------------------------

# Observer Class (Subscriber)
class Subscriber:
    def __init__(self, name):
        # Each subscriber has a name (unique identity)
        self.name = name
        
    def update(self, channel_name, message):
        # This method is called when a channel sends a notification
        print(f"[{channel_name}] -> {self.name} received notification: {message}")


# Subject Class (YouTubeChannel)
class YouTubeChannel:
    def __init__(self, channel_name):
        # Channel name (to identify the publisher)
        self.channel_name = channel_name
        # List of subscribers (observers)
        self.subscribers = []
        
    def subscribe(self, subscriber):
        # Add a subscriber to the list
        if subscriber not in self.subscribers:
            self.subscribers.append(subscriber)
            print(f"{subscriber.name} subscribed to {self.channel_name}.")
        else:
            print(f"{subscriber.name} is already subscribed to {self.channel_name}.")
    
    def unsubscribe(self, subscriber):
        # Remove a subscriber from the list
        if subscriber in self.subscribers:
            self.subscribers.remove(subscriber)
            print(f"{subscriber.name} unsubscribed from {self.channel_name}.")
        else:
            print(f"{subscriber.name} is not subscribed to {self.channel_name}.")
        
    def notify(self, message):
        # Notify all subscribers about a new video/message
        print(f"\n--- Sending Notifications from {self.channel_name} ---")
        for i in self.subscribers:
            i.update(self.channel_name, message)


# -------------------------------
# Client Code (Usage)
# -------------------------------

# 1. Create Subscribers
alice = Subscriber("Alice")
bob = Subscriber("Bob")
charlie = Subscriber("Charlie")

# 2. Create Channels
python_channel = YouTubeChannel("Python Learning Academy")
gaming_channel = YouTubeChannel("Pro Gamer BD")
tech_channel = YouTubeChannel("Tech Review Hub")

print("\n--- Subscription Process ---")
# 3. Subscribe Users to Channels
python_channel.subscribe(alice)
python_channel.subscribe(bob)

gaming_channel.subscribe(bob)
gaming_channel.subscribe(charlie)

tech_channel.subscribe(alice)
tech_channel.subscribe(charlie)

# 4. Upload videos and notify subscribers
python_channel.notify("New Python Tutorial Uploaded!")
gaming_channel.notify("GTA 6 Live Gameplay Started!")
tech_channel.notify("iPhone 18 Review Video Out Now!")

# 5. Unsubscribe Example
print("\n--- Unsubscribe Process ---")
python_channel.unsubscribe(bob)   # Bob leaves Python channel
gaming_channel.unsubscribe(alice) # Alice was never subscribed here
tech_channel.unsubscribe(charlie) # Charlie leaves Tech channel

# 6. Upload again after unsubscribe
python_channel.notify("Advanced Python OOP Concepts Released!")
tech_channel.notify("Laptop Buying Guide 2026 Published!")
