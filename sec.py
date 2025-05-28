# i=1
# for i in range(19):
#     if (i==10):
#         print("skipped iteration")
#         continue
        
#     print("5 X ", i ,"= " ,(5*(i)))


# # def calculateSum(a,b):
# #     sum=a+b
# #     print (sum)

# def calSub(a,b):
#     sub=a-b
#     print (sub)

# def isGreater(a,b):
#     if (a>b):
#         print("a is greater")
#     elif(a<b):
#         print("b is greater")

# def isSmaller(a,b):
#     if (a<b):
#         print("a is smaller")
#     elif(a>b):
#         print("b is smaller")


# a=456
# b=67
# isSmaller(a,b)
# calSub(a,b)
# isGreater(a,b)
# calculateSum(a,b)


def calAvg(*num):
    i=1
    sum=0
    for i in num:
       sum=sum+i
    return sum/len(num)

avg=calAvg(6,5,8)
print(avg, "is the average")


import camelcase
c = camelcase.CamelCase()
txt = "hello world"
print(c.hump(txt))




import numpy
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = numpy.mean(speed)
print(x)
