# einstein.py

def main():
    # Prompt the user for mass as an integer
    mass = int(input("Mass in kilograms: "))

    # Define the speed of light in meters per second
    c = 300_000_000

    # Calculate energy using E = mc^2
    energy = mass * c ** 2

    # Output the result as an integer
    print("Energy in Joules:", energy)

# Call the main function
if __name__ == "__main__":
    main()
