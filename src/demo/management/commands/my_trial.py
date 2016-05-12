from django.core.management.base import BaseCommand, CommandError


from demo.models import *
from datetime import datetime

class Command(BaseCommand):
    def handle(self, *args, **options):
        queue = Queue()
        queue.name = 'test'
        queue.save()

        for i in range(10):
            tweet = Tweets()
            tweet.tweet = 'value: %d'%i
            tweet.save()
            tweets_queue = Tweets_queue()
            tweets_queue.tweet_id = tweet.id
            tweets_queue.queue_id = queue.id
            tweets_queue.time_to_send = datetime.now()
            tweets_queue.save()

        tweetqueue_list = Tweets_queue.objects.filter(queue_id = queue.id)
        #do a foreach loop on tweetqueue_list to get all tweet_ids for retrieving tweets from Tweets table.
        for entry in tweetqueue_list:
            tweets = Tweets.get(id = entry.tweet_id)
            print(tweets.tweet)
