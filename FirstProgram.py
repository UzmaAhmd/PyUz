a="uzma"
aage=29
print("my name is ", a," aage ",aage)
age=int(input("age : "))
if(age<=20):
    print("underage")
elif(age>=20 and age <=30):
    print("adult")
else:
    print("nice")


per=int(input("percentage : "))
pas = "yes" if per<=90 or per>=80 else "no"            #single lne if else
print("grade a with ppercent ",pas)



food=input("Enter food : ")
eat="yes" if food=="apple" else "no"        #single lne if else
print(eat,"you can have the food")


sal=float(input("Enter salary: "))
tax=sal*(0.1,0.2) [sal>50000]               #syntax----> var=(false value, true value) [condition] 
print (tax)

