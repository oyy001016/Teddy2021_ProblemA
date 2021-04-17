import pandas as pd
import numpy as np

file1 = r'C:\Users\oyy\Desktop\泰迪杯2021\A数据\附件1.xlsx'
file2 = r'C:\Users\oyy\Desktop\泰迪杯2021\A数据\附件2(样例数据).csv'


def read_data(file1, file2):
    """
    读取附件1、2中的数据，其中，将附件2的数据的行索引设置为股票编号
    """
    df1 = pd.read_excel(file1)
    df2 = pd.read_csv(file2, index_col=0)
    return df1, df2


def sector_split(df):
    """
    将附件2的数据（df2）按照行业进行划分。
    """
    sector = {}
    for i in range(len(df)):
        stock_num = int(df.iloc[i]['股票代码'])
        stock_sector = df.iloc[i]['所属行业']
        if stock_sector not in sector.keys():
            sector[stock_sector] = []
        sector[stock_sector].append(stock_num)
    return sector


def print_sector(sector):
    for key in sector.keys():
        print(key+':', sector[key])


def sector_assignment(data, sector):
    """
    按行业将股票数据划分并保存到多个表格中。
    """

    cols = list(data.columns)
    for key in sector.keys():
        df = pd.DataFrame(columns=cols)
        for stock_num in sector[key]:
            if stock_num in data.index:
                temp = pd.DataFrame(data.loc[stock_num])
                df = df.append(pd.DataFrame(temp.values.T, index=temp.columns, columns=temp.index))
        s = '\\' + str(key) + '.csv'
        df.to_csv(r'C:\Users\oyy\Desktop\泰迪杯2021'+s)


def read_sector_set():
    sector = np.load('行业划分.npy', allow_pickle=True).item()
    return sector


def read_sector_data(sector_name):
    return pd.read_csv(sector_name + '.csv')


# sector_df, data = read_data(file1, file2)
# sector = sector_split(sector_df)
# print(sector)
# np.save('行业划分.npy', sector)
sector = read_sector_set()
if isinstance(sector, dict):
    for key in sector.keys():
        data = read_sector_data(key)
        print(key+':', len(data))