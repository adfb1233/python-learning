def main():
    text = input("Input: ")
    print("Output:", remove_vowels(text))

def remove_vowels(s):
    vowels = "aeiouAEIOU"
    result = ""
    for char in s:
        if char not in vowels:
            result += char
    return result

if __name__ == "__main__":
    main()
