#Lamda
#var=lamda parameter:statement
add=lambda a,b:a+b
print(add(10,20))

#Ternary operator
#var=if_result.if condition else else_result
var="even" if 10%2==0 else "odd"
print(var)

'''even_li=[]
for i in range(1,21):
    if i%2==0
    even_li.append(i)
    print(even_li)
'''
#even
even_li = [i for i in range(1,21)if i%2==0]
print(even_li)
#pallendrom
pall_li = [i for i in range(100,501) if str(i)==str(i)[::-1]]
print(pall_li )
#odd
odd_li=[i for i in range(0,10)if i%2]
print(odd_li)

#question> li=[[10,20],[78,90],(45,91)]
#li=[[10,20],[78,90],(45,91)]
'''for i in li:
    if type(i)==list:
        for j in i:
            print(j)
        else:
            print(i)'''
#li = [10,20,[78,90],(45,91)]

 #li_new = [10,20,78,90,45,91]
#new_li = [i for sublist in li for i in (sublist if isinstance(sublist,(list,tuple)) else [sublist])]
#print(new_li)

'''tuple=[(23,8),12,34,52,(16,32,183),(15,92)]
#new list=[23,8,12,34,52,16,32,183,15,92]
new_tuple1=[i for i in tuple  ]
#new_tuple=[ i for i in tuple for i in (i if isinstance(i,(list,int))else[i])]
print(new_tuple1)'''

li=[1,2,(89,90),7,8,[95,98]]
new_li = [i for sublist in li for i in (sublist if isinstance(sublist,(list,tuple)) else [sublist])]
print(new_li)




