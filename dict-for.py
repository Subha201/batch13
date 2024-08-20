li=[
    {'Name':'A' , 'Age':26,'Salary':67000,'subject':['python','java','c']},
    {'Name':'B' , 'Age':27,'Salary':89000},
    {'Name':'C' , 'Age':34,'Salary':65000},
    {'Name':'D' , 'Age':33,'Salary':72000},
    {'Name':'E' , 'Age':38,'Salary':60000},
    {'Name':'F' , 'Age':35,'Salary':72000},
    {'Name':'G' , 'Age':31,'Salary':72000},
    {'Name':'H', 'Age':43,'Salary':70000},
]
'''for i in li:
    if i['salary']>=60000 and i['salary']<=70000:
        print(i['Name'],i['Salary'])'''
for i in li:
    if'python' in i['subject']:
        print(i['Name'])