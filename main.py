import pandas as pd


def count(data_list: list) -> tuple:
    count_result = 0
    for item in data_list:
        item_split = item.split("; [")
        count_etc = len(item_split)
        count_russia = len(item_split)
        for elem in item_split:
            if elem.find("Russia") == -1:
                count_etc -= 1
        if count_etc != count_russia:
            count_result += 1
    return count_result, len(data_list)


def main():
    data_df = pd.read_excel("data2020.xls")
    address_list = data_df["Addresses"].to_list()
    value_russia, value_etc = count(address_list)
    print(value_russia/value_etc)