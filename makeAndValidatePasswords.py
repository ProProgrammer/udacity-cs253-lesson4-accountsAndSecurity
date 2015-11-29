import random
import string

# implement the function make_salt() that returns a string of 5 random
# letters use python's random module.
# Note: The string package might be useful here.

def make_salt():
    ###Your code here
    list_random_chars = random.sample(string.ascii_letters, 5)
    return ''.join(str(x) for x in list_random_chars)
    
# print make_salt()

# implement the function make_pw_hash(name, pw) that returns a hashed password 
# of the format: 
# HASH(name + pw + salt),salt
# use sha256

hashed_password_with_salt = ''

def make_pw_hash(name, pw):
    ###Your code here
    salt = make_salt()
    hash_calculated = hashlib.sha256(name + pw + salt).hexdigest()
    hashed_password_with_salt = (hash_calculated + ',' + salt)
    return hashed_password_with_salt

def valid_pw(name, pw, h):
    ###Your code here
    salt_component = h.split(',')[1]
    password_component = h.split(',')[0]
    if hashlib.sha256(name + pw + salt_component).hexdigest() == password_component:
        return True
    else:
        return False

h = make_pw_hash('spez', 'hunter2')
print valid_pw('spez', 'hunter2', h)

