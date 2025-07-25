# -*- coding: utf-8 -*-
"""「Untitled19.ipynb」的副本

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IoNckzqxapEly1sLdD2OMbLimjYzbTJo
"""

import requests
import csv
import pandas as pd

def download_twse_csv(date: str, type_: str = "ALL") -> str:
    """
    Download TWSE daily CSV data as text.

    :param date: Date string in YYYYMMDD
    :param type_: TWSE type, default "ALL"
    :return: CSV raw text
    """
    url = f"https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date={date}&type={type_}&response=csv"
    response = requests.get(url)
    response.encoding = 'cp950'
    if response.status_code != 200:
        raise Exception(f"Failed to download: {response.status_code}")
    print("✅ Download complete")
    return response.text


def extract_csv_lines(raw_text: str) -> list:
    """
    Clean raw text into lines, removing empty and irrelevant ones.
    """
    lines = [line.strip() for line in raw_text.split('\n') if line.strip() and ',' in line]
    print(f"✅ Extracted {len(lines)} non-empty lines")
    return lines


def find_data_section(lines: list, keyword: str = "證券代號") -> (list, list):
    """
    Find header row and data rows starting from the keyword.
    """
    header_idx = None
    for idx, line in enumerate(lines):
        if keyword in line:
            header_idx = idx
            break
    if header_idx is None:
        raise Exception("Could not find header row")
    header_line = lines[header_idx]
    data_lines = lines[header_idx + 1:]
    print(f"✅ Found header at line {header_idx}")
    return header_line, data_lines


def clean_data(header_line: str, data_lines: list) -> pd.DataFrame:
    """
    Convert header and data lines to a cleaned DataFrame.
    """
    header = next(csv.reader([header_line]))
    rows = list(csv.reader(data_lines))
    cleaned_rows = []
    for row in rows:
        cleaned_row = [
            cell.replace('="', '').replace('"', '').strip()
            if cell.startswith('="') else cell.replace('"', '').strip()
            for cell in row
        ]
        cleaned_rows.append(cleaned_row)
    df = pd.DataFrame(cleaned_rows, columns=header)
    print(f"✅ Created DataFrame with shape {df.shape}")
    return df


# 🎯 Example usage
date = "20250702"

raw_text = download_twse_csv(date)
lines = extract_csv_lines(raw_text)
header_line, data_lines = find_data_section(lines)
df = clean_data(header_line, data_lines)

df.head()