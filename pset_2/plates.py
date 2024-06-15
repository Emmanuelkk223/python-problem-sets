def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    punctuation = set("!@#$%^&*()_+{}?><':|./,")
    space = set(" ")
    for char in s:
        if s[2:].isalpha() and max(6, min(2, len(s))) and s[:2].isdigit():
            return True
        elif char in punctuation or char in space:
            return False
main()
