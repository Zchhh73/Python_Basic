import matplotlib.pyplot as plt
from stack_anay.db_access import findall_hisq_data

plt.rcParams['font.family'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def pot_hisvolume(dates, volumes):
    '''股票历史成交量折线图'''

    plt.figure(figsize=(10, 5))
    plt.plot(dates, volumes)

    plt.title('苹果股票历史成交量')
    plt.xlabel('成交日期')
    plt.ylabel('成交量')

    plt.show()


def pot_hosbar(date_list, p_list, ylabel):
    '''绘制柱状图'''

    plt.bar(date_list, p_list)
    plt.title('苹果股票历史成交量')
    plt.xlabel('交易日期')
    plt.ylabel(ylabel)


def main():
    '''
    data = findall_hisq_data('AAPL')
    volume_map = map(lambda it: it['Volume'], data)
    volume_list = list(volume_map)

    date_map = map(lambda it: it['Date'], data)
    date_list = list(date_map)

    pot_hisvolume(date_list, volume_list)
    '''
    data = findall_hisq_data('AAPL')

    date_list = list(map(lambda it: it['Date'], data))
    open_list = list(map(lambda it: it['Open'], data))
    high_list = list(map(lambda it: it['High'], data))
    low_list = list(map(lambda it: it['Low'], data))
    close_list = list(map(lambda it: it['Close'], data))

    plt.figure(figsize=(10, 6))
    plt.subplot(411)
    pot_hosbar(date_list, open_list, '开盘价')
    plt.subplot(412)
    pot_hosbar(date_list, close_list, '收盘价')
    plt.subplot(413)
    pot_hosbar(date_list, high_list, '最高价')
    plt.subplot(414)
    pot_hosbar(date_list, low_list, '最低价')

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
