def main():
    months = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }

    while True:
        try:
            date_str = input("Date: ").strip()

            # Case 1: MM/DD/YYYY format
            if "/" in date_str:
                month, day, year = map(int, date_str.split("/"))

            # Case 2: MonthName D, YYYY format
            elif "," in date_str:
                month_str, day_year = date_str.split(" ", 1)
                day, year = day_year.replace(",", "").split()
                day = int(day)
                year = int(year)
                if month_str not in months:
                    raise ValueError
                month = months[month_str]

            else:
                raise ValueError

            # Validate ranges
            if not (1 <= month <= 12 and 1 <= day <= 31):
                raise ValueError

            # Output formatted date
            print(f"{year:04d}-{month:02d}-{day:02d}")
            break

        except (ValueError, IndexError):
            continue  # Invalid input, prompt again

if __name__ == "__main__":
    main()
