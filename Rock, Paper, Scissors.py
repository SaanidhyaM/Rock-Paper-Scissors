import random
o = ['rock','paper','scissors']
s=random.choice(o)
ans = 'y'
p=0
c=0
while ans!='n':
    b=input("\nYour choice: ").lower()
    while b not in o:
        b=input("Enter a valid choice: ").lower()
    print("Computer's choice:",s)
    if b=='rock':
        if s=='paper':
            print("Paper covers Rock.")
            c+=1
        elif s=='scissors':
            print("Rock smashes Scissors.")
            p+=1
        else:
            print("Draw")
    if b=='paper':
        if s=='scissors':
            print("Scissors cut Paper.")
            c+=1
        elif s=='rock':
            print("Paper covers Rock.")
            p+=1
        else:
            print("Draw")
    if b=='scissors':
        if s=='rock':
            print("Rock smashes Scissors.")
            c+=1
        elif s=='paper':
            print("Scissors Cuts Paper.")
            p+=1
        else:
            print("Draw")
    s = random.choice(o)
    print("\nPlayer score:",p)
    print("Computer score:",c)
    ans = input("\nDo you want to play again? (y/n)")

if p>c:
    print("\nYou win!")
elif c>p:
    print("\nYou lose.")
else:
    print("\nIt's a draw.")
print("\nThank you for playing")
    
