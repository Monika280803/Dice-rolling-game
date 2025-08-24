import random
while True:
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1+die2
    print("You rolled", die1, die2)
    print("Total:", total)
    ans = input("Do you want to play again(y/n)? ").strip().lower()
    if ans not in ('y', 'yes'):
        print("Thanks for playing!")
        break
