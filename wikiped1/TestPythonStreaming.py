# Databricks notebook source
# MAGIC %sh timeout 1 nc 54.213.33.240 9002

# COMMAND ----------

from pyspark.sql.functions import *
from pyspark.sql.streaming import *
from pyspark.sql.types import *
from datetime import datetime
from pyspark.sql import SparkSession

# COMMAND ----------

# MAGIC %sql SET spark.sql.shuffle.partitions = 3 

# COMMAND ----------

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .getOrCreate()

lines = spark.readStream \
    .format("socket") \
    .option("host", "54.213.33.240") \
    .option("port", 9002) \
    .load()

# COMMAND ----------

edits = lines.select(json_tuple('value', "channel", "timestamp", "isRobot", "isAnonymous")) \
  .selectExpr("c0 as channel", "cast(c1 as timestamp) as time", "c2 as page") \
  .createOrReplaceTempView("edits")

# COMMAND ----------

parquetData = sql("select * from edits")
#display(parquetData)


# COMMAND ----------

editCounts = spark.sql("""SELECT count(*), channel, date_format(window(time, '10 seconds').start, 'HH:mm:ss') as time 
                              FROM edits 
                              GROUP BY channel, window(time, '10 seconds')
                              ORDER BY time""")

# COMMAND ----------

#display(editCounts)

# COMMAND ----------

print(editCounts)

# COMMAND ----------

editCounts.describe

# COMMAND ----------


