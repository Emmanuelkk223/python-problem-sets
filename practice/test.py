due = 50
while due > 0:
    coin = int(input("Insert: "))
    if coin in [5, 10, 25, 4]:
        due -= coin
        if due > 0:
            print(f"Amount Due: {due}")
        else:
            print(f"Change owe: {-due}")

    else:
        print("Insert Valid denomination")
