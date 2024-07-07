import matplotlib.pyplot as plt

x_values = range(1,1001)
y_values = [x**2 for x in x_values]

plt.style.use('Solarize_Light2')
fig,ax = plt.subplots()
ax.scatter(x_values,y_values,c=y_values, cmap=plt.cm.cool,s=10) #s definiuje wielkość punktu, c definiuje color

#zdefiniowanie tytułu wykresów i osi
ax.set_title("Kwadraty liczb", fontsize = 20)
ax.set_xlabel("Wartości",fontsize = 12)
ax.set_ylabel("Kwadrat wartości", fontsize = 12)

ax.tick_params(axis="both",which = 'major',labelsize = 10)

#zdefiniowanie zakresów dla każdej osi
ax.axis([0,1100,0,1100000])

plt.show()