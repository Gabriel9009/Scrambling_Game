import random
print("Guess the correct word\n")
name = ["gabriel", "daniel", "solomon", "segun", "opukeme"]

for i in name:
    mylist = list(i)
    random.shuffle(mylist)
    new = ''.join(mylist)

    print(new,"\n")
    name = input()
    if name == i:
        print("\nCorrect")
    else:
        print("Wrong")