'''num1=int(input('enter the first no:-'))
num2=int(input('enter the second no:-'))
print("average= ",(num1+num2)/2)'''

li=[1,2,(89,90),7,8,[95,98]]
'''new_li = [i for sublist in li for i in (sublist if isinstance(sublist,(list,tuple)) else [sublist])]
print(new_li)'''
for i in li:
    if type(i)==list:
        for j in i:
            print(j)
        else:
            print(i)