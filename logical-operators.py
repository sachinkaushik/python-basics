#we have three logical operators
# AND , OR , NOT

high_income = True
good_credit = False

if high_income and good_credit:
    print("Eligble")
else:
    print("Not Eligible")    

#-------------------------------------

if high_income or good_credit:
    print("Eligble")
else:
    print("Not Eligible")    

 #--------------------------------------
 
if not good_credit:
    print("Eligble")
else:
    print("Not Eligible")       