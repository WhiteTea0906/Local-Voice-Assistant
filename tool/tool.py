import random

def sayhi(username):
    greeting = random.choice(["你好", "怎麼了?", "早安"])
    print(f"{greeting} {username}")