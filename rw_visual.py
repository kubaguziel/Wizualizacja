import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    #przygotowanie danych błądzenia losowego i wyświetlenie punktów
    rw = RandomWalk(50000)
    rw.fill_walk()

    #wyświetlenie punktów błądzenia losowego
    plt.style.use('seaborn-v0_8-bright')

    fig, ax = plt.subplots(figsize=(12,9), dpi=128) #wielkość okna wykresu wyrażona w calach
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap='Purples', edgecolors='none',s=1)
    #podkreślenie pierwszego i ostatniego punktu błądzenia losowego
    ax.scatter(0, 0, c='green', edgecolors='none',s=50)
    ax.scatter(rw.x_values[-1],rw.y_values[-1],c='red', edgecolors='none', s=50)

    #ukrywanie osi1
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()
    keep_running = input("Utworzyć kolejne błądzenie losowe? (t/n): ")
    if keep_running == 'n':
        break