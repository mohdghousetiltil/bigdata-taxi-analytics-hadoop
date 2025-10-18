#!/bin/bash

hdfs dfs -rm -r /Output/Task2

hadoop jar ./hadoop-streaming-3.1.4.jar \
    -D mapreduce.job.reduces=3 \
    -input /Input/Trips.txt \
    -output /Output/Task2 \
    -mapper ./Task2mapper.py \
    -reducer ./Task2reducer.py \
    -file ./Task2mapper.py \
    -file ./Task2reducer.py \
    -file ./initialization.txt