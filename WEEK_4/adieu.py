def main():
    names = []

    try:
        while True:
            name = input()
            if name.strip():
                names.append(name.strip())
    except EOFError:
        pass

    print("Adieu, adieu, to", format_names(names))

def format_names(names):
    if len(names) == 1:
        return names[0]
    elif len(names) == 2:
        return f"{names[0]} and {names[1]}"
    else:
        return f"{', '.join(names[:-1])}, and {names[-1]}"

if __name__ == "__main__":
    main()
