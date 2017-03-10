import unittest
import tweepy
import requests
import json

## SI 206 - W17 - HW5
## COMMENT WITH:
## Your section day/time:
## Any names of people you worked with on this assignment:

######## 500 points total ########

## Write code that uses the tweepy library to search for tweets with a phrase of the user's choice (should use the Python input function), and prints out the Tweet text and the created_at value (note that this will be in GMT time) of the first THREE tweets with at least 1 blank line in between each of them, e.g.

## TEXT: I'm an awesome Python programmer.
## CREATED AT: Sat Feb 11 04:28:19 +0000 2017

## TEXT: Go blue!
## CREATED AT: Sun Feb 12 12::35:19 +0000 2017

## .. plus one more.

## You should cache all of the data from this exercise in a file, and submit the cache file along with your assignment. 

## So, for example, if you submit your assignment files, and you have already searched for tweets about "rock climbing", when we run your code, the code should use CACHED data, and should not need to make any new request to the Twitter API. 
## But if, for instance, you have never searched for "bicycles" before you submitted your final files, then if we enter "bicycles" when we run your code, it _should_ make a request to the Twitter API.

## The lecture notes and exercises from this week will be very helpful for this. 
## Because it is dependent on user input, there are no unit tests for this -- we will run your assignments in a batch to grade them!

## We've provided some starter code below, like what is in the class tweepy examples.

## **** For 50 points of extra credit, create another file called twitter_info.py that contains your consumer_key, consumer_secret, access_token, and access_token_secret, import that file here, and use the process we discuss in class to make that information secure! Do NOT add and commit that file to a public GitHub repository.

## **** If you choose not to do that, we strongly advise using authentication information for an 'extra' Twitter account you make just for this class, and not your personal account, because it's not ideal to share your authentication information for a real account that you use frequently.

## Get your secret values to authenticate to Twitter. You may replace each of these with variables rather than filling in the empty strings if you choose to do the secure way for 50 EC points
consumer_key = "NEjeGQrEqAvyMBhZSh9MJ3c98" 
consumer_secret = "jDMPTDipmpN8EmWXzKhNbMrLGjfLSFAYnNl3LesYWyCEFqLF5z"
access_token = "430314150-xczwLPEvmHXNov5hFjMJ3dKsZICUNn3mBL2qCIfg"
access_token_secret = "ueqvbuHr34kTdnvhxHIeGuvILUfYaCP5KkwySFL1aWN3m"
## Set up your authentication to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser()) # Set up library to grab stuff from twitter with your authentication, and return it in a JSON-formatted way

## Write the rest of your code here!

#### Recommended order of tasks: ####
## 1. Set up the caching pattern start -- the dictionary and the try/except statement shown in class.
## 2. Write a function to get twitter data that works with the caching pattern, so it either gets new data or caches data, depending upon what the input to search for is. You can model this off the class exercise from Tuesday.
## 3. Invoke your function, save the return value in a variable, and explore the data you got back!
## 4. With what you learn from the data -- e.g. how exactly to find the text of each tweet in the big nested structure -- write code to print out content from 3 tweets, as shown above.

CACHE_FNAME = 'project2.json' # String for your file. We want the JSON file type, because that way, we can easily get the information into a Python dictionary!
try:
    cache_file = open(CACHE_FNAME, 'r') # Try to read the data from the file
    cache_contents = cache_file.read() # If it's there, get it into a string
    CACHE_DICTION = json.loads(cache_contents) # And then load it into a dictionary
    cache_file.close() # Close the file, we're good, we got the data in a dictionary.
except:
    CACHE_DICTION = {}


def get_tweet_data(phrase):
        unique_identifier = "twitter_{}".format(phrase)
        if unique_identifier in CACHE_DICTION:
                 twitter_results = CACHE_DICTION[unique_identifier]
                 return twitter_results
        else:
                 twitter_results = api.search(phrase)
                 CACHE_DICTION[unique_identifier] = twitter_results
                 f = open(CACHE_FNAME,'w')
                 f.write(json.dumps(CACHE_DICTION))
                 f.close()
                 return twitter_results


#ps = get_tweet_data("python")
#print(ps)

def canonical_order(d):
    alphabetized_keys = sorted(d.keys())
    res = []
    for k in alphabetized_keys:
        res.append((k, d[k]))
    return res
    
# This is the function that actually builds each URL to make a request with, so we can say "Have we made a request with this URL before?" It invokes the  canonical_order function in the process.
def requestURL(baseurl, params = {}):
    req = requests.Request(method = 'GET', url = baseurl, params = canonical_order(params))
    prepped = req.prepare()
    return prepped.url


song_d = json.dumps(CACHE_DICTION, indent = 2)
#print(song_d)

input1 = input("Enter search term: ")
#public_tweets = api.search(q=input1)

#try:
#	x = open('tweets.json', 'r')
#	cache_contents = cache_file.read()
#	cached_data = json.loads(x.read())
#	x.close()
#except:
	
#	f = open('tweets.json', 'w')
#	f.write(json.dumps(public_tweets))
#	f.close()

ps = get_tweet_data(input1)
i = 0
list1 = []
list2 = []
while i <3:
	for key, val in (ps["statuses"][i].items()):
		if key == "created_at":
			list1.append(val)
			i+=1
k=0
while k <3:
	for key, val in (ps["statuses"][i].items()):
		if key == "text":
			list2.append(val)
			k+=1
			

print("TEXT: " + list2[0])
print("CREATED AT: " + list1[0])
print("\n")
print("TEXT: " + list2[1])
print("CREATED AT: " + list1[1])
print("\n")
print("TEXT: " + list2[2])
print("CREATED AT: " + list1[2])
print("\n")









