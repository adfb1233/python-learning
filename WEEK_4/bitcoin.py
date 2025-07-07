import sys
import requests

def main():
    # 驗證命令列是否有且為數字
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    # 使用你提供的 API Key
    api_key = "bd4ee146c9c61279ee2d42beebe9e613794378193f66f965687ae846904b8c96"
    url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}"

    # 向 CoinCap v3 API 查詢
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        sys.exit("Request failed")

    # 解析 JSON 並取出 priceUsd
    data = response.json()
    try:
        price = float(data["data"]["priceUsd"])
    except (KeyError, TypeError, ValueError):
        sys.exit("Unexpected API response")

    # 計算並輸出結果（四位小數 + 千分號）
    cost = n * price
    print(f"${cost:,.4f}")

if __name__ == "__main__":
    main()
