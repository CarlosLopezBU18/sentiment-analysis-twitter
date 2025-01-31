# Análisis de Sentimientos en Tiempo Real con Twitter

## Descripción del Proyecto
Este proyecto consiste en una aplicación en Python que realiza un análisis de sentimientos en tiempo real utilizando tweets. La aplicación se conecta a la API de Twitter, captura tweets en tiempo real, analiza el sentimiento de cada tweet (positivo, negativo o neutral) y visualiza los resultados en un dashboard interactivo.

## Requisitos
1. **Conexión a la API de Twitter**: Utiliza la API de Twitter para capturar tweets en tiempo real.
2. **Análisis de sentimientos**: Aplica técnicas de Procesamiento de Lenguaje Natural (NLP) para analizar el sentimiento de los tweets.
3. **Visualización en tiempo real**: Crea un dashboard interactivo que muestre los resultados del análisis de sentimientos.
4. **Persistencia de datos**: Almacena los tweets y los resultados del análisis en una base de datos para su posterior consulta.

## Tecnologías y Librerías
- **Python 3.8+**
- **Tweepy**: Para conectarse a la API de Twitter y capturar tweets en tiempo real.
- **TextBlob** o **VADER**: Para el análisis de sentimientos.
- **Flask** o **FastAPI**: Para crear un servidor web que sirva el dashboard.
- **SQLite** o **PostgreSQL**: Para almacenar los tweets y los resultados del análisis.
- **Dash** o **Streamlit**: Para crear el dashboard interactivo.
- **Pandas**: Para manipulación de datos.
- **Matplotlib** o **Plotly**: Para visualización de datos.

## Estructura del Proyecto

```
sentiment-analysis-twitter/
│
├── README.md
├── requirements.txt
├── app/
│ ├── init.py
│ ├── twitter_client.py # Conexión a la API de Twitter
│ ├── sentiment_analysis.py # Análisis de sentimientos
│ ├── database.py # Conexión y operaciones con la base de datos
│ ├── dashboard.py # Dashboard interactivo
│ └── config.py # Configuración (API keys, etc.)
├── data/
│ └── tweets.db # Base de datos SQLite
└── tests/ # Pruebas unitarias
├── test_twitter_client.py
├── test_sentiment_analysis.py
└── test_database.py
```


## Instrucciones
1. **Configuración de la API de Twitter**:
   - Crea una cuenta de desarrollador en Twitter y obtén las credenciales de la API (API Key, API Secret Key, Access Token, Access Token Secret).
   - Configura estas credenciales en `app/config.py`.

2. **Captura de tweets**:
   - Utiliza `Tweepy` para conectarte a la API de Twitter y capturar tweets en tiempo real basados en un hashtag o palabra clave específica.

3. **Análisis de sentimientos**:
   - Implementa el análisis de sentimientos utilizando `TextBlob` o `VADER`. Cada tweet debe ser clasificado como positivo, negativo o neutral.

4. **Persistencia de datos**:
   - Almacena los tweets y los resultados del análisis en una base de datos SQLite o PostgreSQL.

5. **Dashboard interactivo**:
   - Crea un dashboard utilizando `Dash` o `Streamlit` que muestre:
     - Gráficos en tiempo real de la distribución de sentimientos.
     - Una lista de los últimos tweets analizados.
     - Estadísticas generales (por ejemplo, porcentaje de tweets positivos, negativos y neutrales).

6. **Pruebas**:
   - Escribe pruebas unitarias para cada módulo de la aplicación.
