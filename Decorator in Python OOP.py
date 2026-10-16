# ১. মূল কফি ইন্টারফেস/ক্লাস
class Coffee:
    def get_cost(self):
        return 50  # বেস কফির দাম ৫০ টাকা
        
    def get_description(self):
        return "প্লেইন কফি"

# ২. ডেকোরেটর বেস ক্লাস (যা কফি অবজেক্টকে মুড়িয়ে রাখবে)
class CoffeeDecorator(Coffee):
    def __init__(self, coffee_object):
        self._coffee = coffee_object

    def get_cost(self):
        return self._coffee.get_cost()

    def get_description(self):
        return self._coffee.get_description()

# ৩. সুনির্দিষ্ট ডেকোরেটর ১: দুধ (Milk)
class MilkDecorator(CoffeeDecorator):
    def get_cost(self):
        return self._coffee.get_cost() + 20  # দুধের জন্য ২০ টাকা যোগ হবে

    def get_description(self):
        return self._coffee.get_description() + " + দুধ"

# ৪. সুনির্দিষ্ট ডেকোরেটর ২: ক্যারামেল (Caramel)
class CaramelDecorator(CoffeeDecorator):
    def get_cost(self):
        return self._coffee.get_cost() + 30  # ক্যারামেলের জন্য ৩০ টাকা যোগ হবে

    def get_description(self):
        return self._coffee.get_description() + " + ক্যারামেল"

# --- ব্যবহার (Client Code) ---

# প্রথমে একটি সাধারণ কফি নিলাম
my_coffee = Coffee()
print(f"অর্ডার: {my_coffee.get_description()} | দাম: {my_coffee.get_cost()} টাকা")

# কফিতে দুধ যোগ করলাম (ডেকোরেট করলাম)
milk_coffee = MilkDecorator(my_coffee)
print(f"অর্ডার: {milk_coffee.get_description()} | দাম: {milk_coffee.get_cost()} — টাকা")

# এবার দুধ-কফিতে ক্যারামেলও যোগ করলাম
fancy_coffee = CaramelDecorator(milk_coffee)
print(f"অর্ডার: {fancy_coffee.get_description()} | দাম: {fancy_coffee.get_cost()} টাকা")
