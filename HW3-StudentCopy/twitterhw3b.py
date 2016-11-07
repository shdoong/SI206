# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.
import tweepy
from textblob import TextBlob
import re

# Unique code from Twitter
#Access tokens taken out to commit to git

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
#Now we can Create Tweets, Delete Tweets, and Find Twitter Users
search = input("Enter Twitter search term: ")
public_tweets = api.search(search)

sentiment = []
total_pol = 0
total_sub = 0

for tweet in public_tweets:
	print(tweet.text.encode("ascii", "ignore").decode("utf-8"))
	analysis = TextBlob(tweet.text)
	sentiment.append(analysis.sentiment)
	total_pol += analysis.sentiment.polarity
	total_sub += analysis.sentiment.subjectivity

print ("")
print("Average subjectivity is " + str(total_sub/len(sentiment)))
print("Average polarity is " + str(total_pol/len(sentiment)))
