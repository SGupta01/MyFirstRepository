''' Problem Statment: You need to Spin the letter provided by the user.
if the letter is 5 character or more then only letter will spinned or reversed else not

example: 
this is a cat -> this is a cat
this is my first code -> this is my tsrif code

***Solution***
'''

def spin_word(item):
    str = ""
    if len(item) >=5:
         for x in item:
            str = x + str
    else:
        for x in item:
            str = str + x
    return str
        
T = input("Kindly provide the letters or sentance to be Spinned :")

list_item = T.split(" ")
sp = ""
for item in list_item:
    i = str(spin_word(item))
    sp = sp + " " + i     
print (sp)
