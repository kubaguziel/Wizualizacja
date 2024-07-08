import csv 
from datetime import datetime 

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    #pobranie temperatur maksymalnych z pliku
    dates, highs, lows  = [],[],[]
    for row in reader:
        current_date = datetime.strptime(row[2],"%Y-%m-%d")
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

#przygotowanie wykresu
plt.style.use('Solarize_Light2')
fig,ax = plt.subplots()
ax.plot(dates,highs,c = 'red',linewidth = 1)
ax.plot(dates,lows,c='blue', linewidth = 1)
ax.fill_between(dates,highs,lows,facecolor = 'purple', alpha = 0.2)

#formatowanie wykresu
ax.set_title("Najwyższa i najniższa temperatura dnia,2018", fontsize = 24)
ax.set_xlabel('',fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperatura(F)',fontsize = 16)
ax.tick_params(axis='both',which='major',labelsize = 16)


plt.show()