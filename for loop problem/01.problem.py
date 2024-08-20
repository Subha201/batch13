#for
num=int(input("enter the number:-"))
for i in range(1,11):
    #print(str(num)+ "X" + str(i) + '='+ str(i*num))
    print(f'{num}x{i}={num*i}')

#while
num=int(input("enter your number:-"))
i=0
while i<=10:
    print(f'{num}x{i}={num*i}')
    i=i+1
