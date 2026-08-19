# A countdown using a while loop

count = 5

while count > 0:
    print(count)
    count = count - 1

print("Blast off !!!")

# Building a simple rep counter

for rep in range(1, 6):
    print(f"This is rep no. {rep}")

# A guessing game 

secret_word = "python"

while True:
    guess = input("guess the programming language: ").lower()
    if guess == secret_word:
        print("You guessed it right!")
        break
    else:
        print("Try again!")
