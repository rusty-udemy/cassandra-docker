# myapp/models.py

import uuid
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

class Tweets(Model):
    id = columns.UUID(primary_key=True, default=uuid.uuid4)
    tweet = columns.Text()
    description = columns.Text()
    created = columns.DateTime()
    modified = columns.DateTime()

class Queue(Model):
    id = columns.UUID(primary_key=True, default=uuid.uuid4)
    name = columns.Text()
    created = columns.DateTime()
    modified = columns.DateTime()

class Tweets_queue(Model):
    queue_id = columns.UUID(primary_key=True)
    time_to_send = columns.DateTime(primary_key=True, clustering_order="DESC")
    tweet_id = columns.UUID(primary_key=True, clustering_order="ASC")

class Queue_tweet_responses(Model):
    queue_id = columns.UUID(primary_key=True)
    time_received = columns.TimeUUID(primary_key=True, clustering_order="DESC")
    tweet_id = columns.UUID()
    response = columns.Text()

class Tweets_sent(Model):
    queue_id = columns.UUID(primary_key=True)
    time_sent = columns.DateTime(primary_key=True, clustering_order="DESC")
    tweet_id = columns.UUID()
