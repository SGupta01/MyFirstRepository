'''
Ask user to input thier name and age.
based on the inputs provided by the user, print a msg to back to the user when (year) they will reach 100 yrs.
'''
from datetime import datetime
user_Name = input("Kindly provide you name ")
user_age = int(input("How old are you? :"))


Yrs_left = 100 - user_age
current_yr = datetime.now().year

Yrs_100 = current_yr + Yrs_left

print("Hey " + user_Name +", you will be 100 years old in the year " + str(Yrs_100))

