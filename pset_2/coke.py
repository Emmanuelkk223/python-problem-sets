def coke_machine():
    due = 50
    while due > 0:
        coin = int(input("insert coin: "))
        if coin in [25, 10, 5]:
            due -= coin
            if due > 0:
                print(f"Amount due: {due}")
            else:
                print(f"Change: {-due}")

        else:
            print("Invalid coin")

coke_machine()
