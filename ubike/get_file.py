import csv
import requests
import datetime

CSV_URL = 'http://data.ntpc.gov.tw/od/data/api/54DDDC93-589C-4858-9C95-18B2046CC1FC?$format=csv'


with requests.Session() as s:
    download = s.get(CSV_URL)

    decoded_content = download.content.decode('utf-8')

    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
    # for row in my_list:
    #     print(row)
    # print(my_list[0])
    file_name = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    f = open('/home/qoo/Documents/ubike/data/' + file_name + '.csv', "w")
    w = csv.writer(f)
    w.writerows(my_list)
    f.close()