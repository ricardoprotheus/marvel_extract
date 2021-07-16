import pandas as pd

from functions.functions import criar_lista_herois


# dados que serão utilizados no DataFrame
data = criar_lista_herois()


# definindo colunas do df e dados que serão inseridos
df = pd.DataFrame(
    columns=['id', 'hero_name', 'description', 'comics_count', 'series_count', 'stories_count', 'events_count'],
    data=data)


# criação de arquivo csv com os dados
df.to_csv('heroes.csv', index=False, sep=';')
