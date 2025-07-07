import sys
import pyfiglet
import random

def main():
    fonts = pyfiglet.Figlet().getFonts()  # 相容所有版本

    if len(sys.argv) == 1:
        font = random.choice(fonts)
    elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
        font = sys.argv[2]
        if font not in fonts:
            sys.exit("Invalid font")
    else:
        sys.exit("Usage: figlet.py [-f FONT]")

    text = input("Input: ")

    try:
        fig = pyfiglet.Figlet(font=font)
        print(fig.renderText(text))
    except pyfiglet.FontNotFound:
        sys.exit("Invalid font")

if __name__ == "__main__":
    main()
