#!/usr/bin/env python2
import datetime
import time
import twitter

def prime(n):
    "Returns 1 if n is prime, returns 0 otherwise"
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True

def primeBiggerThan(p):
    p = p + 1
    while not prime(p):
        p = p + 1
    return p

config = {}
execfile("twitterConfig.py", config)
api = twitter.Api(config["consumer_key"], config["consumer_secret"], config["access_token_key"], config["access_token_secret"])

user = api.VerifyCredentials()
statuses = api.GetUserTimeline(user_id=id, count=1)
p = 0
last = 0
if statuses:
    p = int(statuses[0].text)
    last = datetime.datetime.strptime(statuses[0].created_at,'%a %b %d %H:%M:%S +0000 %Y')
    print "It will start to tweet prime numbers bigger than %s" % p

timeBetweenTweets = datetime.timedelta(0, seconds=8*60*60)
delta = datetime.datetime.utcnow() - last
if delta < timeBetweenTweets:
    time.sleep(timeBetweenTweets.total_seconds() - delta.total_seconds())

p = primeBiggerThan(p)
while(1):
    status = api.PostUpdate(p)
    print "Twitter status update: %s" % p
    p = primeBiggerThan(p)
    
    statuses = api.GetUserTimeline(user_id=id, count=1)
    last = datetime.datetime.strptime(statuses[0].created_at,'%a %b %d %H:%M:%S +0000 %Y')
    
    delta = datetime.datetime.utcnow() - last
    if delta < timeBetweenTweets:
        time.sleep(timeBetweenTweets.total_seconds() - delta.total_seconds())
