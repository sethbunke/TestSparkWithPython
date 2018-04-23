# Import dependencies
#    Print to stdout
from __future__ import print_function
#    Spark
from pyspark import SparkContext
#    Spark Streaming
from pyspark.streaming import StreamingContext
#    Kafka
from pyspark.streaming.kafka import KafkaUtils
#    json parsing
import json

# Create Spark context
sc = SparkContext(appName="PythonStreamingDirectKafkaWordCountRM")
# Create Streaming context, with a batch duration of 10 seconds
# ref: http://spark.apache.org/docs/latest/api/python/pyspark.streaming.html#pyspark.streaming.StreamingContext
# ref: http://spark.apache.org/docs/latest/streaming-programming-guide.html#initializing-streamingcontext
ssc = StreamingContext(sc, 10)

# Connect to Kafka, topic 'twitter', consumer group 'spark-streaming'
# ref: http://spark.apache.org/docs/latest/streaming-kafka-0-8-integration.html
kafkaStream = KafkaUtils.createStream(ssc, 'kafka-zk:2181', 'spark-streaming', {'twitter':1})

# Parse the inbound message as json
parsed = kafkaStream.map(lambda v: json.loads(v[1]))

# Count the number of instance of each tweet text
text_counts = parsed.map(lambda tweet: (tweet['text'],1)).\
  reduceByKey(lambda x,y: x + y)
# Print the text counts (first ten shown)
text_counts.pprint()

# Count the number of tweets per author
author_counts = parsed.map(lambda tweet: (tweet['user']['screen_name'],1)).\
  reduceByKey(lambda x,y: x + y)

# Print the author tweet counts (first ten shown)
author_counts.pprint()

# Start the streaming context
ssc.start()
ssc.awaitTermination()