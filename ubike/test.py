import pandas as pd
from os import listdir
import matplotlib
import matplotlib.pyplot as plt

file_names = [f for f in listdir('data')]
file_names.sort()

can_borrow = {}
can_return = {}
areas = ['板橋區']
sites = ['板橋車站', '捷運板橋站(3號出口)', '捷運板橋站(1號出口)', '新北市政府(新府路)', '新北市政府(新站路)',
 '板橋福德公園', '國光里', '板橋戶政事務所', '板橋地政事務所', '縣民民族路口', '捷運府中站(2號出口)', '捷運府中站(3號出口)']
key = 'snaen'
total_bikes = {}

for file_name in file_names:
    df = pd.read_csv('data/' + file_name)
    for i, row in df.iterrows():
        if row['sna'] in sites:
            total_bikes[row['sna']] = row['tot']
            if row[key] in can_borrow:
                can_borrow[row[key]].append(row['sbi'])
            else:
                can_borrow[row[key]] = [row['sbi']]
            if row[key] in can_return:
                can_return[row[key]].append(row['bemp'])
            else:
                can_return[row[key]] = [row['bemp']]
    
# print(can_borrow)
# print(can_return)

# print(total_bikes)

time_tick = [f[:-7] for f in file_names]
for i, v in can_borrow.items():
    plt.xticks(range(len(file_names)), time_tick, rotation='vertical')
    plt.plot(v, label=i)
plt.legend(bbox_to_anchor=(1.1, 1.1), loc=1, borderaxespad=0.)
plt.show()

# for i, v in can_return.items():
#     plt.xticks(range(len(file_names)), time_tick, rotation='vertical')
#     plt.plot(v, label=i)
# plt.legend(bbox_to_anchor=(1, 1), loc=1, borderaxespad=0.)
# plt.show()

print(can_borrow.keys())
plt.bar(range(len(file_names)), can_borrow['MRT Banqiao Sta.(Exit.1)'])
plt.xticks(range(len(file_names)), time_tick, rotation='vertical')
plt.show()
