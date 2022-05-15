#Question 1
a="Python is a case sensitive language"
#a
print(len(a))
#b
rev=a[length::-1]
print("reverse string:",rev)
#c
n=input(a[10:26])
print(n)
#d
replace_str=a.replce("a case sensitive","object oriented")
print("Replaced string:",replace_str)
#e
i=a.find("a")
print("Index of a:",i)
#f
x=a.remove(" ")
print(x)


#Question 2
name=input("Enter your name:")
new_name="Hey, %s here!"%(name)
sid=input("Enter your SID:")
new_sid=("My SID is %d"%(sid))
dep=input("Enter your department:")
cgpa=float(input("Enter your cgpa"))
dc="I am from %s department and my cgpa is %f"%(dep,cgpa)
print(new_name)
print(new_sid)
print(dc)


#Question 3
a=56
b=10
#a
print("a&b:",(a&b))
#b
print("a|b:"(a|b))
#c
print("a^b:",(a^b))
#d
print("Left shift a by 2:"(a<<2))
print("Left shift b by 2:"(b<<2))
#e
print("Right shift a by 2:"(a>>2))
print("Right shift b by 4:"(b>>4))

#Question 4
x=input("Enter something:")
if "name" in x:
    print(Yes)
else:
    print(No)

#Question 5
l1=int(input())
l2=int(input())
l3=int(input())
while l1+l2>l3 or l1+l3>l2 or l2+l3>l1:
    print("yes")
    break
while l1+l2<=l3 or l2+l3<=l1 or l3+l1<=l2:
    print("No")
    break

#Question 6
n1=int(input("Enter number a:"))
n2=int(input("Enter b number:"))
count=0
while(n1>0 or n2>0):
    temp1=n1&1
    temp2=n2&1
    if temp1!=temp2:
        count+=1
        s1=s1>>1
        s2=s2>>1
    print(count)
