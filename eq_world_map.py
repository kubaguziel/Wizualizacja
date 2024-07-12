import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

#analiza struktury danych
filename = "A:\programowanie\python\Wizualizacja\data\eq_data_30_day_m1.json"

with open(filename) as f:
    all_eq_data = json.load(f)
    readable_file = 'data/readable_eq_data.json'
    with open(readable_file, 'w') as f:
        json.dump(all_eq_data,f,indent=4) #indent = 4 nakazuje funkcji .dump sformatownaie danych z wykorzystaniem wcięć dopasowanych do struktury danych

    all_eq_dicts = all_eq_data['features'] #pobiera dane związane z kluczem 'features' i umieszczamy je w słowniku all_eq_dicts
    print(len(all_eq_dicts))
    mags,lons,lats,hover_texts = [],[],[],[]

    for eq_dict in all_eq_dicts:
        mag = eq_dict['properties']['mag']
        lon = eq_dict['geometry']['coordinates'][0]
        lat = eq_dict['geometry']['coordinates'][1] 
        title = eq_dict['properties']['title']     
        mags.append(mag)
        lons.append(lon)
        lats.append(lat)
        hover_texts.append(title)


    #Mapa trzęsień ziemi
    data = [{
        'type':'scattergeo',
        'lon':lons, #długości geograficzne 
        'lat':lats, #szerokości geograficzne
        'text':hover_texts,
        'marker': {
            'size': [6*mag for mag in mags], #wykorzystujemy listę składaną
            'color':mags,   #wartości, które powinny być uzywane podczas ustalania, czy dany punkt mieści się na skali kolorów 
            'colorscale':'Electric',
            'reversescale':True, #ponieważ kolor żółty ma być stosowany do najmniejszych wartości
            'colorbar':{'title':'Siła'}
    }, }] 
    my_layout = Layout(title="Trzęsienia ziemi na świecie")
    
    fig = {'data':data,'layout':my_layout}
    offline.plot(fig,filename='global_earthquakes.html')