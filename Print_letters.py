
'Printing Letter "E"'

for row in range(5):
    for col in range(5):
        if col >0 and (row == 1 or row == 3):
            print (" ",end = "")
        else:
            print("*", end = "")
            
    print("")
    
'Printing Letter "A"'
for row in range(5):
    for col in range(5):
        if (col >0 and col <4) and (row == 1 or row == 3 or row ==4):
            print (" ",end = "")
        else:
            print("*", end = "")
            
    print("")
