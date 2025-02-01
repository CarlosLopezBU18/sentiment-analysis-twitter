import tweepy as tw
from config import APIConfig

client = tw.Client(bearer_token=APIConfig.BEARER_TOKEN,
                   consumer_key=APIConfig.API_KEY, 
                   consumer_secret=APIConfig.API_KEY_SECRET, 
                   access_token=APIConfig.ACCESS_TOKEN,     
                   access_token_secret=APIConfig.ACCESS_TOKEN_SECRET,
                   wait_on_rate_limit=True)


user = client.get_user(username='elonmusk')  # Example public account
print(user.data['id'])
fl = client.get_users_followers(id=user.data['id'], user_auth=True)
print(fl)