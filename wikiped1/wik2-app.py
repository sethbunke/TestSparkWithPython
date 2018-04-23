#%%sh timeout 1 nc 54.213.33.240 9002

from pyspark.sql.functions import *
from pyspark.sql.streaming import *
from pyspark.sql.types import *
from datetime import datetime

from pyspark.sql import SparkSession
from pyspark.sql import *
from pyspark.sql.functions import explode
from pyspark.sql.functions import split

from pyspark import SparkContext
from pyspark.streaming import StreamingContext

#%sql SET spark.sql.shuffle.partitions = 3 

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .getOrCreate()
    #.config("spark.some.config.option", "some-value") \
    

lines = spark.readStream \
    .format("socket") \
    .option("host", "54.213.33.240") \
    .option("port", 9002) \
    .load()

edits = lines.select(json_tuple('value', "channel", "timestamp", "isRobot", "isAnonymous")) \
  .selectExpr("c0 as channel", "cast(c1 as timestamp) as time", "c2 as page") \
  .createOrReplaceTempView("edits")

parquetData = sql("select * from edits")
#display(parquetData)

editCounts = spark.sql("""SELECT count(*), channel, date_format(window(time, '10 seconds').start, 'HH:mm:ss') as time 
                              FROM edits 
                              GROUP BY channel, window(time, '10 seconds')
                              ORDER BY time""")

#display(editCounts)


