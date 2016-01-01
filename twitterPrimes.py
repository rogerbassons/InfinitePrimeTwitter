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
if statuses:
    p = int(statuses[0].text)
print "It will start to tweet prime numbers bigger than %s" % p

seconds = 8*60*60 # every 8 hours
t = datetime.datetime.now()
delta = datetime.timedelta(0, seconds)
while(1):
    p = primeBiggerThan(p)
    status = api.PostUpdate(p)
    print "Twitter status update: %s" % p
    while datetime.datetime.now() - t < delta:
        time.sleep(seconds/2)
    t = datetime.datetime.now()

    
