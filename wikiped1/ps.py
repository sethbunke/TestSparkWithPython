



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

#sc = StreamingContext()

sc = SparkContext(appName="PythonTwitterStreaming")
ssc = StreamingContext(sc, 1)
#lines = ssc.socketTextStream("54.213.33.240", 9002)

stream = ssc.socketTextStream("https://streamer.cryptocompare.com/", 443)

stream.pprint()

#print(lines)

ssc.start()
ssc.awaitTermination()



#ssc = new StreamingContext("local[2]", "NodejsTcpClient", Seconds(1))

#val lines = ssc.socketTextStream("127.0.0.1", 1337, StorageLevel.MEMORY_AND_DISK_SER)

#lines.print()






