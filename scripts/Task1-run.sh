#!/bin/bash    
hadoop jar ./hadoop-streaming-3.1.4.jar \
-D mapred.reduce.tasks=3 \
-file ./Task1mapper.py \
-mapper ./Task1mapper.py \
-file ./Task1reducer.py \
-reducer ./Task1reducer.py \
-input /Input/Trips.txt \
-output /Output/Task1