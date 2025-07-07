def main():
    grocery_list = {}

    try:
        while True:
            item = input().strip().lower()
            if item:
                grocery_list[item] = grocery_list.get(item, 0) + 1
    except EOFError:
        pass

    for item in sorted(grocery_list):
        print(f"{grocery_list[item]} {item.upper()}")

if __name__ == "__main__":
    main()
