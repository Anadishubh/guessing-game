import random

while True: 

    secret_number = random.randint(1, 10)
    attempts = 0
    max_attempts = 5

    print("\n🎮 Welcome to the Guessing Game!")
    print("Guess a number between 1 and 10")

    while attempts < max_attempts:  # Guessing loop

        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess == secret_number:
            print(f"🎉 Correct! You guessed it in {attempts} attempts.")
            break

        elif guess < secret_number:
            print("📉 Too low!")

        else:
            print("📈 Too high!")

        print(f"Attempts left: {max_attempts - attempts}")

    if attempts == max_attempts and guess != secret_number:
        print(f"😞 Game Over! The correct number was {secret_number}.")

    play_again = input("Play again? (y/n): ")

    if play_again.lower() != "y":
        print("👋 Thanks for playing!")
        break