import random

print("🎯 Welcome to the Guessing Game!")
name = input("What's your name? ")
print(f"Nice to meet you, {name}! Let's start 😄")

high_score = None  # أقل عدد محاولات لتخمين صحيح

while True:
    pc_choice = random.randint(1, 10)
    attempts = 0

    print("\nI've picked a number between 1 and 10. Try to guess it!")

    while True:
        try:
            user_choice = int(input("Your guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if not 1 <= user_choice <= 10:
            print("Number must be between 1 and 10!")
            continue

        attempts += 1

        if user_choice == pc_choice:
            print(f"🎉 Correct! The number was {pc_choice}. You got it in {attempts} attempts.")
            if high_score is None or attempts < high_score:
                high_score = attempts
                print(f"🏆 New High Score! ({high_score} attempts)")
            else:
                print(f"💡 Your best score is still {high_score} attempts.")
            break
        elif user_choice < pc_choice:
            print("Too low! Try higher 🔼")
        else:
            print("Too high! Try lower 🔽")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print(f"\nThanks for playing, {name}! 👋")
        if high_score:
            print(f"Your best score was {high_score} attempts.")
        break
