lst1=[[1, 2], [3, 4], [5, 6, 7],[[1,2,3,[4,5,6,[7,8]]],9,10]]

def kontrol(i):
    if type(i)==list:
        i.reverse()
        for j in i:
            kontrol(j)

lst1.reverse()
for i in lst1:
    kontrol(i)
print(lst1)