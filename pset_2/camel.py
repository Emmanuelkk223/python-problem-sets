def main():
    camel_case = input("camelCase: ")
    snake_case = camel(camel_case)
    print(f"snake_case: {snake_case}")
def camel(c):
    snake_case = ''
    for char in c:
        if char.isupper():
            if snake_case:
                snake_case += '_'
            snake_case += char.lower()
        else:
            snake_case += char
    return snake_case

main()
