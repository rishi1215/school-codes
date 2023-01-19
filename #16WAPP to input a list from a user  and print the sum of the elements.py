#WAPP to input a list from a user  and print the sum of the elements
L=[]
L1=int(input("enter the number of  elements :"))
for i in range(L1):
    n=int(input("enter the  elements"))
    L.append(n)
print(L)
sum=0
for x in L:
      sum+=x
print(sum)
  
  
