def main():
    amount_due = 50
    accepted_coins = [25, 10, 5]

    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        coin = int(input("Insert Coin: "))
        if coin in accepted_coins:
            amount_due -= coin
        else:
            print("Invalid coin.")

    change = abs(amount_due)
    print(f"Change Owed: {change}")

if __name__ == "__main__":
    main()
