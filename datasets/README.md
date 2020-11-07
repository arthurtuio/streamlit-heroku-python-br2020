# Pasta dos Datasets

Pasta criada para armazenar datasets que você poderá usar
durante o seu projeto do Streamlit.
 
Estes datasets viram do Kaggle: 

- [`WA_Fn-UseC_-HR-Employee-Attrition`](https://www.kaggle.com/pavansubhasht/ibm-hr-analytics-attrition-dataset)
- [`Nutrition Facts for McDonald's Menu`](https://www.kaggle.com/mcdonalds/nutrition-facts)
- [`Spotify Song Attributes`](https://www.kaggle.com/geomack/spotifyclassification)
- [`Chocolate Bar Ratings`](https://www.kaggle.com/rtatman/chocolate-bar-ratings)
- [`Uber Drives`](https://www.kaggle.com/zusmani/uberdrives)
- [`New York City Airbnb Open Data`](https://www.kaggle.com/dgomonov/new-york-city-airbnb-open-data)

Você pode fazer uma exploração inicial dos mesmos direto do Google Colab:
> [Como usar a API do Kaggle no Google Colab](https://colab.research.google.com/github/corrieann/kaggle/blob/master/kaggle_api_in_colab.ipynb#scrollTo=L7ZmFbHybsPk)

Caso queira apenas conferir suas colunas e uma amostra dos registros, acesse o arquivo exploracao_inicial_datasets

Para importar os datasets direto no seu projeto, importe o arquivo load_dataframe.py, dessa forma:
```
from load_dataframe import LoadDataframe

x_dataset = LoadDataframe.dataset()
```