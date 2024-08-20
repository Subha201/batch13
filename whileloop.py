#while True:
    #print(1)

'''i = 0
while i<10:
 print("yes" + str(i))
 i=i+1
print("Done")'''

i=0
while i<=50:
    print(i)
    i=i+1
print("Done")

'''i=0
while i<5:
    print("subha"+str(i))
    i=i+1

fruits=["banana","apple","grapes","mangoes"]
i=0
while i<=len(fruits):
    print(fruits[i])
    i=i+1'''

#Write a pallendrom number with help of while loop without using string?

#121 , 313,333,666,......
i=int(input("enter your number:-"))
rev = 0
x=i
while (i>0):
    rev = (rev*10)+i%10
    i=i//10
if(x==rev):
    print(x,"is palindrome number")
else:
    print(x,"is not palindrome number")

print("happy")

#write a program  to find the sum of first n natural numbers using while loop?
'''num=int(input("enter N value:-"))
sum=0
while (num>0):
    sum=sum+num
    num=num-1
    print("sum of  N natural number" , sum)'''
   
