list = []
x = int(input("tole list: "))

for i in range(x):
    araye = int(input("adad morede nazar khod ra vared konid: "))
    list.append(araye)

print(list)

for j in range(1 ,len(list)):
    if list[j] > list[j-1]:
        print("moratab")
        
    else:
        print("namoratab")
