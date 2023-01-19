#WAPP to input n numbers from the user. Store these numbers in a tuple. Print the maximum, minimum, sum and mean of number from this tuple
t=()
n=int(input("enter the max length of the list"))
for i in range(n):
    x=int(input("Enter the value:"))
    t+=(x,)
print(t)
print(type(t))
ma=t[0]
for i in t:
    if  ma<i:
        ma=i
print("maximum value in the tuple is:",ma)
mi=t[0]
for i in t:
    if mi>i:
        mi=i
print("minimum value in the list is;",mi)
add=0
for i in t:
    add+=i
print("sum of the elements is :",add)
print("average of the elemetns in the list is :",add/(len(t)))

