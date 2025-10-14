from randomuser import RandomUser
import pandas as pd

#tao doi tuong
r = RandomUser()

#tao ra 10 buc anh nguoi ngau nhien
some_list = r.generate_users(10)
for user in some_list:
    print(user.get_picture())