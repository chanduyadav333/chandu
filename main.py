# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
print(1+2+3)
a="chandu"
print(len(a))
print("python\tis\tamazing\n")
b=input()
c=input()
print(len(b+c))
list1=[1,2,3,4]
print(list1)
la=[1,2]
lb=[3,la]
la[1]=0
print(la)
print(lb)
num="1 234"
nl=num.split()
print(nl)
a=[1,2,3,4,56,7]
n=a[7:0:-1]
print(n)
m=int(input())
n=int(input())
l=[]
for i in range(0,n):
    l.append(m)
print(l)
a=int(input())
l=[]
for i in range(0,a):
    b=int(input())
    l.append(b)
print(l[0:3:1])
print(l[-3:a:1])