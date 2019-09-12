
from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import get_data.twitter_credentials as credentials

#ツイッタークライアント
class TwitterClient():
    def __init__(self,twitter_user=None):
        #認証
        self.auth=TwitterAuthenticator().authenticate_twitter_app()
        #APIクライアント
        self.twitter_client=API(self.auth)
        #ユーザの指定
        self.twitter_user=twitter_user

    def get_user_timeline_tweets(self,num_tweets):
        tweets=[]
        #APIクライアントのユーザタイムラインをcursorオブジェクトにして、ページネーション処理
        for tweet in Cursor(self.twitter_client.user_timeline,id=self.twitter_user).items(num_tweets):
            tweets.append(tweet)
        return tweets

    def get_friend_list(self,num_friends):
        friend_list=[]
        for friend in Cursor(self.twitter_client.friends,id=self.twitter_user).items(num_friends):
            friend_list.append(friend)

        return friend_list

    def get_home_timeline_tweets(self,num_tweets):
        home_timeline_tweets=[]
        for tweet in Cursor(self.twitter_client.home_timeline,id=self.twitter_user).items(num_tweets):
            home_timeline_tweets.append(tweet)
        return home_timeline_tweets

#ツイッター認証

class TwitterAuthenticator():

    def authenticate_twitter_app(self):
        auth=OAuthHandler(credentials.consumer_key,credentials.consumer_secret)
        auth.set_access_token(credentials.Access_token,credentials.Access_secret)
        return auth

#ツイッターストリーミング

class TwitterStreamer():

    def __init__(self):
        self.twitter_authenticator=TwitterAuthenticator()

        def stream_tweets(self,fetched_tweets_filename,hash_tag_list):
            listener=TwitterListener(fetched_tweets_filename)
            auth=self.twitter_authenticator.authenticate_twitter_app()
            stream=Stream(auth,listener)

            stream.filter(track=hash_tag_list)

#ツイッターリスナー

class TwitterListener(StreamListener):

    def __init__(self,fetched_tweets_filename):
        self.fetched_tweet_filename=fetched_tweets_filename

    def on_data(self, raw_data):
        try:
            print(data)
            with open(self.fetched_tweet_filename,'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True

    def on_error(self, status):
        if status==420:
            return False
        print(status)


if __name__ == '__main__':

    hash_tag_list=["gunsandroses","nirvana","beatles"]
    fetched_tweets_filename="tweets_bands.txt"

    twitter_client=TwitterClient('reo61210449')
    print(twitter_client.get_user_timeline_tweets(1))
    print(twitter_client.get_home_timeline_tweets(10))
    print(twitter_client.get_friend_list(10))



