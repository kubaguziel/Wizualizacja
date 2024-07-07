import matplotlib.pyplot as plt

input_values = [1,2,3,4,5]
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn-v0_8-darkgrid')

fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=2)

ax.set_title("Kwadraty liczb 1-5", fontsize = 20)
ax.set_xlabel("Wartość", fontsize = 14)
ax.set_ylabel("Kwadrat wartości", fontsize = 14)

#zdefiniowanie wartości etykiet
ax.tick_params(axis='both',labelsize = 12)

plt.show()