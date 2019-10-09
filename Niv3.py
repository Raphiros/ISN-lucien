import random

x = 0
score = 0
operation = ["add", "sub", "mul"]

for x in range(10):

    nb1 = random.randint(0, 100)
    nb2 = random.randint(0, 100)
    ops = random.choice(operation)
    if (ops == "add"):
        print(nb1, "+", nb2)
        solUser = int(input("Solution?"))
        solution = nb1 + nb2
        if solution == solUser:
            print("Bravo!")
            score += 1
        else:
            print("Solution = ", solution)

    elif (ops == "sub"):
        print(nb1, "-", nb2)
        solUser = int(input("Solution?"))
        solution = nb1 - nb2
        if solution == solUser:
            print("Bravo!")
            score += 1
        else:
            print("Solution = ", solution)

    elif (ops == "mul"):
        print(nb1, "*", nb2)
        solUser = int(input("Solution?"))
        solution = nb1 * nb2
        if solution == solUser:
            print("Bravo!")
            score += 1
        else:
            print("Solution = ", solution)

print("Score: ", score, "/10")
