# -------------------------------
# Factory Method Pattern in Python
# -------------------------------
# GOF (Gang of Four) Design Pattern
# Intent: Define an interface for creating an object,
# but let subclasses decide which class to instantiate.
# -------------------------------

# ১. Base / Interface Class (Optional but Good Practice)
class Notification:
    def send(self, message):
        # Base method (abstract-like)
        # এখানে শুধু কাঠামো দেওয়া হলো, আসল কাজ করবে concrete ক্লাসগুলো
        pass


# ২. Concrete Classes (যারা আসল কাজ করবে)
class SMSNotification(Notification):
    def send(self, message):
        # SMS এর মাধ্যমে মেসেজ পাঠানোর লজিক
        return f"SMS এর মাধ্যমে পাঠানো হলো: {message}"

class EmailNotification(Notification):
    def send(self, message):
        # Email এর মাধ্যমে মেসেজ পাঠানোর লজিক
        return f"Email এর মাধ্যমে পাঠানো হলো: {message}"


# ৩. Factory Class (যা অবজেক্ট তৈরি করবে)
class NotificationFactory:
    @staticmethod
    def create_notification(type):
        # Factory Method: ইউজারের ইনপুট অনুযায়ী সঠিক অবজেক্ট তৈরি করবে
        if type.lower() == "sms":
            return SMSNotification()
        elif type.lower() == "email":
            return EmailNotification()
        else:
            # যদি ভুল টাইপ দেওয়া হয়, তাহলে error ছুঁড়ে দিবে
            raise ValueError("ভুল নোটিফিকেশন টাইপ!")


# -------------------------------
# Client Code (যেখানে এটি ব্যবহার করা হবে)
# -------------------------------

# আমাদের সরাসরি SMSNotification বা EmailNotification ক্লাস কল করতে হচ্ছে না
# আমরা শুধু Factory কে বলছি আমাদের কী চাই।
notification_type = "sms"   # এটি ইউজারের ইনপুট হতে পারে
msg_object = NotificationFactory.create_notification(notification_type)

# Factory থেকে পাওয়া অবজেক্ট দিয়ে কাজ করা হচ্ছে
print(msg_object.send("হ্যালো, কেমন আছেন?"))
