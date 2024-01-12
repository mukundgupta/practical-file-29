n = int(input("Enter number of friends: "))

names = []
num = []
for i in range(1,n+1):
    na = input("Enter name {}".format(i))
    names.append(na)

for i in range(0,n):
    nu = input("Enter number of {}".format(names[i]))
    num.append(nu)

d = dict(zip(names,num))
print(d)


new = input("Add new name: ")
d[new] = input("Enter number: ")
print(d)

de = input("Enter name to delete: ")
del d[de]
print(d)

mod = input("Enter name of friend whose number to modify: ")
d[mod] = input("Enter new number: ")
print(d)

se = input("Enter name to search: ")
print("Searching...")

if se in d:
    print(se," exists in dictionary")
else:
    print(se," does not exist in dictionary")    


ds = sorted(d)
print('Sorted dictionary: ',ds)