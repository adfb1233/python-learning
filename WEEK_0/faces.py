def convert(text):
    # :) 轉換為 🙂，:( 轉換為 🙁
    return text.replace(":)", "🙂").replace(":(", "🙁")

def main():
    # 提示使用者輸入文字
    user_input = input("Input some word（include :) or :(）：")
    # 呼叫 convert 並印出結果
    print(convert(user_input))

# 呼叫 main 函數
if __name__ == "__main__":
    main()
