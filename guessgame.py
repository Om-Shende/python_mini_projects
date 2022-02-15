import random
r1 = random.randint(0, 10)
i = None
print(r1)
while i != r1:
    i = int(input("try to guess a number between 0-10:"))
    if i > r1:
        print("your answer was to high")

    elif i < r1:
        print("your answer was very low")

    else:
        print("congrats you guess it right")
