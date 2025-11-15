import random

total_attempts=[]
attempts=0
pc_choice=random.randint(1,10)

print("Welcome To The Gussing Game!")
name=input("What's Your Name?: ")
wanna_play=input(f"nice to meet you {name}, Want To Start? (Yes,No): ").lower()
while True:
    if wanna_play=="no":
        print("Oh I'm Sad :(")
        if  total_attempts :
            print(f"this is your score {min(total_attempts)}")

        elif not total_attempts :
            print("There is No Score ")
            exit()         
    elif wanna_play=="yes":
        print("Good Let's Go! ")
        while True:
            try:
                user_choice=int(input("selesct Number Between 1 and 10: "))
                attempts+=1
                if user_choice < 1 or user_choice > 10:
                    raise ValueError("invaild Number ")
                elif user_choice == pc_choice:
                    print("Wow You Get It Right! ")
                    total_attempts.append(attempts)
                    attempts=0
                    pc_choice=random.randint(1,10)
                    wanna_play = input("Do you want to play again? (Yes,No): ").lower()
                    if wanna_play == "no":
                        break
                    elif wanna_play=="yes":
                        continue
                    else:
                        print("invaild enter ")

                elif user_choice < pc_choice:
                    print("Higher!")
                elif user_choice > pc_choice:
                    print("Lower! ")    
                else:
                    print("invaild enter ")
                    wanna_play = input("Do you want to play again? (Yes,No): ").lower()
            except ValueError as err:
                print("please enter a number 1:10 ")
    else:
        print("invaild enter ")
        wanna_play=input(f"nice to meet you {name}, Want To Start? (Yes,No): ").lower()