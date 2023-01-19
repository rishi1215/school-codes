import random
count=3
ans='y'
win =False
print("Guess the number ,computer generated between 20-30")
print("Total 3 chances are there")
print("--------------------------------------------------------------------------------")
while ans=='y':
    num1=random.randint(20,30)
    print("chance remaining: ",count)
    guess=int(input("Enter your answer:"))
    if  num1==guess:
        print("Congratulations!, You guessed it right")
        win =True
    else:
        print('wrong!')
        count-=1
        if count==0:
            print('Oops! You lost all your chances ')
            print('number was: ',num1)
    if win==True or count==0:
        ans=input('Play again?')
        if ans=='y':
            count=3
            win=False
