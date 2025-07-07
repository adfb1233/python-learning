import sys
import pyfiglet
import random

def main():
    fonts = pyfiglet.getFonts()

    if len(sys.argv) == 1:
        font = random.choice(fonts)
    elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
        font = sys.argv[2]
        if font not in fonts:
            sys.exit("Invalid font.")
    else:
        sys.exit("Usage: figlet.py [-f FONT]")

    text = input("Input: ")
    ascii_art = pyfiglet.figlet_format(text, font=font)
    print("Output:")
    print(ascii_art)

if __name__ == "__main__":
    main()

