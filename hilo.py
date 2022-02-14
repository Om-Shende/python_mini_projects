low = 1
high = 1000
print("Guess a number between {} and {}".format(low, high))
guesses = 0

while True:
    print("\tGuessing the number between {} and {}".format(low, high))
    guess = low + (high - low) // 2
    high_low = input(
        "my guess is {}. should i go higher or lower? enter h or l, c if my guess is correct".format(guess)).casefold()
    if high_low == "h":
        low = guess + 1
    elif high_low == "l":
        high = guess - 1
    elif high_low == "c":
        print("guessed the value")
        break
    else:
        print("please enter h.l or c")
    guesses += 1
