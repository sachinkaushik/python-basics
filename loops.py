for number in range(3):
    print("Attempt" , number)



#-------------------------------------------
    
successful = True
for n in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break;

#---------------------------------------------

successful = False
for n in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break;
else:
    print("Attempted 3 times and failed........")

#--------------------------------------------------
for x in range(5):   
    for y in range(3):
        print(f"({x}, {y})")

