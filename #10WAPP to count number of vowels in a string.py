#WAPP to count number of vowels in a string
vowels='aeiouAEIOU'
str=input("enter the string:")
count=0
for i in str:
    if i in vowels:
        count+=1
print("number of vowels in the string are:",count)
