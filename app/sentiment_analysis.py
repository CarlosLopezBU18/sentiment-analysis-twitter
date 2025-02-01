from nltk.sentiment.vader import SentimentIntensityAnalyzer
from config import SAConfig

def download_vader():
    from nltk import download
    download(SAConfig.SENTIMENT_ANALIZER)   

analyzer = SentimentIntensityAnalyzer()
sc = analyzer.polarity_scores("I love dogs")
print(sc)
