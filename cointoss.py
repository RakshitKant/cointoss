import random as rand
def cointoss(num):
    heads=0
    for _  in range(0,num):
        result=rand.randint(0,1)
        if(result==0):
            print("heads")
            heads+=1
        else:
            print("tails")
            
    return heads
userchoice=input("do you want to toss a coin y/n?")
heads,tails=0,0
if(userchoice=="y"):
    while True:
        try:
         num=int(input("enter the number"))
         heads=cointoss(num)
         tails=num-heads
         print(heads,"number  of heads")
         print(tails,"number of tails")
        except ValueError:
            print('invalid choice')
    
elif(userchoice=="n"):
    print("bye thanks")
else:
    print("enter a valid choice")
