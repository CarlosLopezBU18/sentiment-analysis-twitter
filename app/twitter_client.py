import tweepy as tw
from config import APIConfig

# auth = tw.OAuth1UserHandler(APIConfig.API_KEY, APIConfig.API_KEY_SECRET, APIConfig.ACCESS_TOKEN, APIConfig.ACCESS_TOKEN_SECRET)

# api = tw.API(auth=auth)

client = tw.Client(bearer_token=APIConfig.BEARER_TOKEN, 
                   consumer_key=APIConfig.API_KEY, 
                   consumer_secret=APIConfig.API_KEY_SECRET, 
                   access_token=APIConfig.ACCESS_TOKEN, 
                   access_token_secret=APIConfig.ACCESS_TOKEN_SECRET,
                   wait_on_rate_limit=True)

X = client.get_user(username='X')
id = X.data['id']

tweets = client.get_users_tweets(id=id)

print(tweets.data)