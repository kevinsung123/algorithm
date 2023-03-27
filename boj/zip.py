def Print(a):
    for y in range(3):
        for x in range(3):
            print(a[y][x], end=" ")
        print()


if __name__ == '__main__':
    a = [[(y * 3) + (x + 1) for x in range(3)] for y in range(3)]
    Print(a)
    print("===============")
    A, B, C = list(zip(*a))
    print(A)
    print(B)
    print(C)
    b = list(map(list, zip(*a)))
    Print(b)
    c = list(map(list, zip(*b)))
    print("===============")
    Print(c)

    # Ex3: unzipping the value Using zip
    coordinate = ['x', 'y', 'z']
    value = [3, 4, 5]

    result = zip(coordinate, value)
    result_list = list(result)
    print(result_list)

    c, v = zip(*result_list)
    print('c =', c)
    print('v =', v)
    print("zipping Example================================")
# Python code to demonstrate the application of
# zip()

# initializing list of players.
players = ["Sachin", "Sehwag", "Gambhir", "Dravid", "Raina"]

# initializing their scores
scores = [100, 15, 17, 28, 43]
# printing players and scores.
for pl, sc in zip(players, scores):
    print("Player :  %s     Score : %d" % (pl, sc))
