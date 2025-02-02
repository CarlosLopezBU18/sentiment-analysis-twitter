from nltk.sentiment.vader import SentimentIntensityAnalyzer
from config import SAConfig

def download_vader():
    from nltk import download
    download(SAConfig.SENTIMENT_ANALIZER)   

def analize_message(text: str):
    analyzer = SentimentIntensityAnalyzer()
    return analyzer.polarity_scores(text)