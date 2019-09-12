from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


import get_data.twitter_credentials as credentials


class TwitterStreamer():
    """
    ライブのツイートをストリーム処理するクラス
    """
    def __init__(self):
        pass

    def stream_tweets(self,fetched_tweets_filename,hash_tag_list):
    # This handles Twitter authentication and the connection to the Twitter Streaming API
        listener = StdOutListener(fetched_tweets_filename)
        auth = OAuthHandler(credentials.consumer_key, credentials.consumer_secret)
        auth.set_access_token(credentials.Access_token, credentials.Access_secret)
        stream = Stream(auth, listener)
        stream.filter(track=hash_tag_list)


class StdOutListener(StreamListener):
    """
    基本のリスナークラス：受け取ったツイートをそのまま出力する
    """
    def __init__(self,fetched_tweets_filename):
        self.fetched_tweets_filename=fetched_tweets_filename

    def on_data(self,data):
        try:
            print(data)
            with open(self.fetched_tweets_filename,'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Eror on data: &s" % str(e))
        return True

        print(data)
        return True

    def on_error(self, status):
        print(status)

if __name__ =="__main__":
    hash_tag_list=["nike","adidas"]
    fetched_tweets_filename="tweets.json"

    twitter_streamer=TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename,hash_tag_list)