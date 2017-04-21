# beijing_2016
import csv
import matplotlib.dates
from datetime import datetime
from matplotlib import pyplot as plt


def date_to_list(data_index):
    """ save date to a list """
    results = []
    for row in data:
        results.append(datetime.strptime(row[data_index], '%Y-%m-%d'))
    return results

def data_to_list(data_index):
    """ save data to a list """
    results = []
    for row in data:
        results.append(int(row[data_index]))
    return results


filename = 'beijing_2016.csv'
with open(filename) as bj:
    data = csv.reader(bj)
    header = next(data)

    # print(header)
    # print(next(data))

    # get the index of data needed
    print('date_akdt', header.index('date_akdt'))
    print('high_temp_f', header.index('high_temp_f'))
    print('low_temp_f', header.index('low_temp_f'))


    # create a list from the remaining contents in the iterable
    data = list(data)

    # save data to list
    high_temp_f_bj = data_to_list(1)
    high_temp_c_bj = [int((x-32)/1.8) for x in high_temp_f_bj]

    low_temp_f_bj = data_to_list(3)
    low_temp_c_bj = [int((x-32)/1.8) for x in low_temp_f_bj]

    date = date_to_list(0)


    plt.figure(figsize=(12, 5), dpi=100)
    plt.plot(date, high_temp_c_bj, c='xkcd:orange')
    plt.plot(date, low_temp_c_bj,c='xkcd:azure')

    plt.title('Beijing Temperatures (High & Low) - Year 2016', fontsize=22)
    plt.ylabel('Temperature (C)', fontsize=20)
    plt.tick_params(axis='both', labelsize=16)
    plt.fill_between(date, high_temp_c_bj, low_temp_c_bj, facecolor='xkcd:silver', alpha=0.2)

    plt.gca().xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%Y-%m"))
    plt.gcf().autofmt_xdate()
    plt.margins(x=0,y=0.2)

    plt.show()