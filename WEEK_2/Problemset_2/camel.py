def camel_to_snake(name):
    snake = ""
    for char in name:
        if char.isupper():
            snake += "_" + char.lower()
        else:
            snake += char
    return snake

def main():
    camel = input("camelCase: ")
    snake = camel_to_snake(camel)
    print("snake_case:", snake)

if __name__ == "__main__":
    main()
