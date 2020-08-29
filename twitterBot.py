import tweepy
import time

auth = tweepy.OAuthHandler('zsvgsWBM4Tt99dk7q9N5DvfXy','3dNVlRkPJxTxmdqIrdpPPEFbegNqecYD41Rjg7qzm2RK3rFGC5')
auth.set_access_token('1296803437254856705-EETzfLKYEyXsl5k7qzWBSD7Fg1J0Tg','QN4w4twSixb2b44MP1V8CzbGjuS90mAYhiDgK30RM9q9p')

api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

user = api.me()
#print(user)
print("user is:")
print(user.screen_name)

for follower in tweepy.Cursor(api.followers).items():

    print("followers of you:")
    print(follower.name)


search = 'javascript'
numberTweets = 3
for tweet in tweepy.Cursor(api.search,search).items(numberTweets):
    try:
        print('tweets realated to your search:'+search+":")
        print(tweet)
        #tweet.favorite()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break    


    
