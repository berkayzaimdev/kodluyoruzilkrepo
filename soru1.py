lst=[[1,'a',['cat'],2],[[[3]],'dog'],4,5,(7,8,(9,10,((11))))]
lst2=[]

def kontrol(i):
    if type(i)==list:
        for j in i:
            kontrol(j)
    elif type(i)==tuple:
        for j in i:
            kontrol(j)
    else:
        lst2.append(i)

for i in lst:
    kontrol(i)
    
print(lst2)
    
    

        




