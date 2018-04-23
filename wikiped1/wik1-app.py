
import sys
import time
import json
#import psutil

from pyspark import SparkContext
from pyspark.streaming import StreamingContext

from pyspark.streaming.kafka import KafkaUtils
#from websocket import create_connection


def takeAndPrint(time, rdd, num=1000):
    result = []
    taken = rdd.take(num + 1)
    url = 'ws://localhost:8888/'

    print("-------------------------------------------")
    print("Time: %s" % time)
    print("-------------------------------------------")

    for record in taken[:num]:
    	print(record)
    	result.append(record)

    # ws = create_connection(url)
    # ws.send(json.dumps(result))
    # ws.close()

    if len(taken) > num:
        print("...")
    print("")

def updateFunc(new_values, last_sum):
        return sum(new_values) + (last_sum or 0)

sc = SparkContext(appName="PythonTwitterStreaming")
ssc = StreamingContext(sc, 1)

kvs = KafkaUtils.createStream(ssc, '54.213.33.240:9002', "spark-streaming-consumer", {'iphone': 1})
tweets = kvs.map(lambda x: x[1])

ssc.checkpoint("./checkpoint-tweet")

# edits = lines.select(json_tuple('value', "channel", "timestamp", "isRobot", "isAnonymous")) \
#   .selectExpr("c0 as channel", "cast(c1 as timestamp) as time", "c2 as page") \
#   .createOrReplaceTempView("edits")

# running_counts = tweets.flatMap(lambda line: line.split(" "))\
#                           .map(lambda word: (word, 1))\
#                           .updateStateByKey(updateFunc).transform(lambda rdd: rdd.sortBy(lambda x: x[1],False))


# running_counts.foreachRDD(takeAndPrint)

ssc.start()
ssc.awaitTermination()