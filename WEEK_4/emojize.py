import emoji

def main():
    user_input = input("Input: ")
    output = emoji.emojize(user_input, language="alias")  # 支援 :thumbsup: 等 alias
    print(f"Output: {output}")

if __name__ == "__main__":
    main()
