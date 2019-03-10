import matplotlib.pyplot as plt
import numpy as np
from datetime import date

# INPUT
###########################
begin_date = date(1945,1,1)
###########################


with open("sp500.csv", 'r') as f:
    lines = f.readlines()

header = lines[0].split(',')

time_col = header.index('Date')
price_col = header.index('SP500')

time = []
price = []

for line in lines[1:]:
    l = line.split(',')
    time_str = l[time_col]
    year = int(time_str.split('-')[0])
    month = int(time_str.split('-')[1])
    day = int(time_str.split('-')[2])

    time.append(date(year, month, day))
    price.append(float(l[price_col]))

begin_idx = 0
while time[begin_idx] < begin_date:
    begin_idx += 1

time = np.array(time[begin_idx:])
price = np.array(price[begin_idx:])

elapsed_time = np.array([(x - begin_date).days/365.24 for x in time])
p = np.polyfit(elapsed_time, np.log(price), 1)

plt.plot(time, price, color="black", label="S&P 500, unadjusted")


best_fit = np.array([np.exp(x*p[0] + p[1]) for x in elapsed_time])

plt.plot(time, best_fit, color='red', alpha=0.7,
         label="${0:0.1f} \ e^{{{1:0.3f} \ (t-{2})}}$".format(np.exp(p[1]), np.exp(p[0]), begin_date.year))

plt.xlim(begin_date, date(2020,1,1))
plt.title("Economic Growth, Post-WWII")
plt.xlabel("t")
plt.yscale('log')
plt.legend(loc=2)
plt.savefig("sp.pdf")







