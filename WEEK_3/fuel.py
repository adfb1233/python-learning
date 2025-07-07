def main():
    while True:
        try:
            fraction = input("Fraction: ")
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)

            if y == 0 or x > y:
                raise ValueError

            percentage = round((x / y) * 100)

            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")
            break  # exit loop if input is valid

        except (ValueError, ZeroDivisionError):
            continue  # ask again if input is invalid

if __name__ == "__main__":
    main()
