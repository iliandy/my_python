from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

#consumer key, consumer secret, access token, access secret
ckey = "wQLwOaVFStgnHTY3TrpuSysgo"
csecret = "RdHPmaRm8gL5s66SaE2SBMz6nxqZYkejBqCFDi56iw4zcxC7Vj"
atoken = "887008815681597442-2KlD2oHZHJSEX9SzXpjklYIxWvEZXU4"
asecret = "KVAKCDmGEREAG4qk5aImqhBd6PWF1mmsQPH9JMEYhpEvc"

class listener(StreamListener):
    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["#wodedevtest"])
