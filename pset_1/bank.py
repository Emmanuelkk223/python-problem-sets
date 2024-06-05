def main():
    greetings = input("Greetings: ")
    greetings = greetings.lower()
    greetings = m(greetings)
    print(greetings)

def m(n):
    if n.startswith("hello"):
        return "$0"
    elif n.startswith("hey") or n.startswith("how"):
        return "$20"
    else:
        return "$100"
    
if __name__ == "__main__":
    main()
