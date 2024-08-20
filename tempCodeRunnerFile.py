tuple=[(23,8),12,34,52,(16,32,183),(15,92)]
#new list=[23,8,12,34,52,16,32,183,15,92]
new_tuple1=[i for i in tuple  ]
#new_tuple=[ i for i in tuple for i in (i if isinstance(i,(list,int))else[i])]
print(new_tuple1)