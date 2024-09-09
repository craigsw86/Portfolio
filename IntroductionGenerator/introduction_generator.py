import sys, random

print ("Welcome to the 'Hoity-Toity Introduction Generator.'\n")
print ("A name which sounds more impressive than it really is, just because it mentions where you hail from:\n\n")

first = ('Adam', 'Malcolm', 'Zachary')

last = ('Anderson', 'Smith', 'Weinstein')

place = ('Arkanas', 'Connecticut', 'Wyoming')

while True:
    firstName = random.choice(first)
    lastName = random.choice(last)
    hailingFrom = random.choice(place)
    
    print("\n\n")
    print("Ladies & Gentlemen, we are pleased to introduce {} {} of {}!".format(firstName, lastName, hailingFrom), file=sys.stderr)
    print("\n\n")
    
    try_again = input("\n\nTry again? (Press Enter else n to quit)\n")
    if try_again.lower() == "n":
        break

input("\nPress Enter to exit.")