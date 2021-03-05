import tweepy
from hex_drone_twitter.drone_stream_listener import DroneStreamListener
from hex_drone_twitter.drone_response_pattern import DroneResponsePattern
from hex_drone_twitter.secret import *

from hex_drone_twitter.logs import get_logger
logger = get_logger(__name__)


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

itself = api.me()

response_pattern = DroneResponsePattern('3064')
stream_listener = DroneStreamListener(api, response_pattern, itself)
stream = tweepy.Stream(api.auth, stream_listener)
stream.filter(track=[f'@{itself.screen_name}'], is_async=True)
# user = api.me()
# stream.filter(track=[user.id_str], is_async=True)
