import string
import random

def randomString(n: int):
    random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=n))
    return random_string
