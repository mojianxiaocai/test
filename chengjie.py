#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import csv
import datetime
#http://www.tweepy.org/
import tweepy

# #Get your Twitter API credentials and enter them here
# consumer_key = "4zCY4b6jetELH8CsjF9ZsxkRm"
# consumer_secret = "Y6j3TWaFV2ZjgHBHFwY6JQvXedt1b7GBT0fkx29eGmKmMNvL0t"
# access_key = "458923957-Oe10Wuwo9O4GjubSxJmdZrACCOfo9j2rqITSeCUU"
# access_secret = "oMcPsTbo41sWxvbIEuWT0QQWG12cRv9K6DRVeTAFsGolB"

#Get your Twitter API credentials and enter them here
consumer_key = "uvGxtAoxq8jDk3F8RUUb8XJlb"
consumer_secret = "TYIZyhiJDRUnYHQhqv3p4JqBrYmP6uSykrUJ6ColwCPFQ318p5"
access_key = "828985931222888448-eTFwyhrU5zVJ5scIOSg7Wz1dT6H2Op2"
access_secret = "ltjWK9Rmmyrv2xWuH4XrbtQMRndgEWKgFUTGu4C2PmolR"

# #Get your Twitter API credentials and enter them here
# consumer_key = "QV6on0tAbWLwxdMwtvAH0S0U4"
# consumer_secret = "LoTqMRUnwXcYrgJUlldyDLk395Sw7pGT6DnvjIEieQWovozMZ0"
# access_key = "828987397115359233-P55GSdxUfyUKHJGXZAvM3xnzCfcSKg5"
# access_secret = "0bmfopLAKS9GLvJePkmf2rBuaosayzZGWJ4rJ4UG0E2y8"


# #Get your Twitter API credentials and enter them here
# consumer_key = "2bI95EoRK30MIFfHvWexjYlFR"
# consumer_secret = "E76B2oypVohCj3RwMkOEFh4PVeE0wwNwElpjtlUDTh6IT7q5Z9"
# access_key = "828996149080162304-YRRAux3XTGAEzejkQOSV0ALx98AxgRN"
# access_secret = "0BmrbhQbSWST2MJp0m6uyCEXxlK1TCjfEqNjVYhNTBdLI"


#http://tweepy.readthedocs.org/en/v3.1.0/getting_started.html#api
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
ids=[472876860, 18799647, 19676513, 551541843,187227496,136717652, 709161518621917184, 2676512838,
424446736, 2894523731, 344664377, 22798473, 337292268, 1538141425, 241273855, 2597701569, 3354846525,
34057667, 394607278, 3684024141, 185603644, 707345900, 17603748, 20446182, 2338445082, 115743614, 1706744972,
743672940,99164177]

# ids =[293033687,437639054, 1541537562,586941998, 378166508, 2243880350;90463990, 31136820,479000231,
# 550337463,371966407,907396904,479904593, 395816770, 4797669281, 369113389， 26235399, 341091227
# 374104061, 408677947, 483118429, 3835147769, 3826268535;758993088, 58174573, 271550265, 887461298, 178641583, 62863357
# 37202977, 46807460, 299204774, 41708161, 395995376]

#have more than 600 tweets in 8 weeks: 3077551160, 506407977, 3112082646, 876358518, 2726059382, 28772094, 989452274, 52877126
#472876860, 18799647, 19676513, 551541843,187227496,136717652, 709161518621917184, 2676512838,
#424446736, 2894523731, 344664377, 22798473, 337292268, 1538141425, 241273855, 2597701569, 3354846525
#34057667, 394607278, 3684024141, 185603644, 707345900, 17603748, 20446182, 2338445082, 115743614, 1706744972
#743672940,99164177


# with open( 'xuhui.csv', 'w') as f:
# 	writer = csv.writer(f)
# 	data = ['username','week 1','week 2','week 3','week 4','week 5', 'week 6','week 7', 'week 8']
# 	writer.writerow(data)

#method to get a user's last 100 tweets
def get_tweets(userid):
	user=api.get_user(userid)
	username = user.screen_name	
	print "writing to {0}_tweets.csv".format(userid)
	if (user.followers_count>80 and user.friends_count>40 and user.statuses_count>200):
		number_of_tweets = 200
		tweets = api.user_timeline(id = username,count = number_of_tweets)
		tweets_for_time=[tweet.created_at for tweet in tweets]
		tweets_length=[len(tweet.text) for tweet in tweets]
		length=[0,0,0,0,0,0,0,0]
		days=datetime.date(2017,2,14)-tweets_for_time[len(tweets_for_time)-1].date()
		if days.days>56:
			for i in range(len(tweets_for_time)):
				days=datetime.date(2017,2,14)-tweets_for_time[i].date()
				if days.days<7:
					length[0]=length[0]+tweets_length[i]
				elif 7<=days.days<14:
					length[1]=length[1]+tweets_length[i]
				elif 14<=days.days<21:
					length[2]=length[2]+tweets_length[i]
				elif 21<=days.days<28:
					length[3]=length[3]+tweets_length[i]
				elif 28<=days.days<35:
					length[4]=length[4]+tweets_length[i]
				elif 35<=days.days<42:
					length[5]=length[5]+tweets_length[i]
				elif 42<=days.days<49:
					length[6]=length[6]+tweets_length[i]
				elif 49<=days.days<56:
					length[7]=length[7]+tweets_length[i]

			with open( 'xuhui1.csv', 'ab') as f:
				writer = csv.writer(f)
				data = [username,length[0],length[1],length[2],length[3],length[4],length[5],length[6],length[7]]
				writer.writerow(data)
		else:
				print "user {0} have more than 200 tweets in 8 weeks".format(userid)




for i in range(len(ids)):
	get_tweets(ids[i])


