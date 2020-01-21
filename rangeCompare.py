import random

highest = 100 
answer = random.randint(1,highest) 
print("answer is ", answer)

x = int(input("Enter the number btw 1 & {} : ".format(highest))) 
attempt = 0 
flag=0 

while True:

    attempt=attempt+1

    if x==answer:
        print("got it ")
        break
    elif attempt==3:
        flag=1
        print("exceeded attempts")
        break
    elif x>answer:
        print("enter lower")
        x=int(input("enter number"))

    elif x<answer:
        print("enter larger")
        x=int(input("enter number"))

