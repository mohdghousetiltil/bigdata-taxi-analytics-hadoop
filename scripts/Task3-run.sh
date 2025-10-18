#!/bin/bash 

# Run the first MapReduce job   
hadoop jar ./hadoop-streaming-3.1.4.jar \
-D mapred.reduce.tasks=3 \
-file ./Task3mapper1.py \
-mapper ./Task3mapper1.py \
-file ./Task3reducer1.py \
-reducer ./Task3reducer1.py \
-input /Input/Trips.txt,/Input/Taxis.txt \
-output /Output/Task3_joinop

# Run the second MapReduce job
hadoop jar ./hadoop-streaming-3.1.4.jar \
-D mapred.reduce.tasks=3 \
-file ./Task3mapper2.py \
-mapper ./Task3mapper2.py \
-file ./Task3reducer2.py \
-reducer ./Task3reducer2.py \
-input /Output/Task3_joinop \
-output /Output/Task3_countop

# Run the third MapReduce job
hadoop jar ./hadoop-streaming-3.1.4.jar \
-D mapred.reduce.tasks=1 \
-file ./Task3mapper3.py \
-mapper ./Task3mapper3.py \
-file ./Task3reducer3.py \
-reducer ./Task3reducer3.py \
-input /Output/Task3_countop \
-output /Output/Task3

# Clean up intermediate output directories
hdfs dfs -rm -r /Output/Task3_joinop
hdfs dfs -rm -r /Output/Task3_countop