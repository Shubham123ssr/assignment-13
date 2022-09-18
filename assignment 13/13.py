'''
#q1

mylist=["Java","python","sql","c"]
print(mylist)

#q2
print(type(mylist))
#q3
print(mylist[-1])
#q4
mylist.insert(3,"Reactnative")
print(mylist)
#q5
mylist.append("C++")
print(mylist)
#q6
secondlist=["c#","js","html"]
#mylist.append(secondlist)
#print(mylist)
#q7
'''
'''
for e in mylist:
    print(e)
    '''
#q8
'''
mylist.sort()
print(mylist)
'''
#q9
'''
# creating an empty list
lst = []
# number of elemetns as input
n = int(input("Enter number of elements : "))
# iterating till the range
for i in range(0, n):
            ele = int(input())
            lst.append(ele) # adding the element
print(lst)
'''
#q10
'''
lst=[]
a=int(input("Enter the value of a "))
b=int(input("Enter the value of b "))
for i in range(a,b):

    d=a%10
    a=a+1
    lst.append(d)
print(lst)
'''
