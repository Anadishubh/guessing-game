import random

while True: 

    secret_number = random.randint(1, 10)
    attempts = 0

    print("\n🎮 Welcome to the Guessing Game!")
    print("Guess a number between 1 and 10")

    while True:  # Guessing loop

        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess == secret_number:
            print(f"🎉 Correct! You guessed it in {attempts} attempts.")
            break

        elif guess < secret_number:
            print("📉 Too low!")

        else:
            print("📈 Too high!")

    play_again = input("Play again? (y/n): ")

    if play_again.lower() != "y":
        print("👋 Thanks for playing!")
        break