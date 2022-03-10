STREAM_JAR_PATH="/root/hadoop/app/hadoop-3.3.2/share/hadoop/tools/lib/hadoop-streaming-3.3.2.jar" #hadoop streaming jar 包所在的位置
INPUT_FILE_PATH="/test/test.txt"  #要进行词频统计的文档在hdfs中的路径
OUTPUT_PATH="/output"        #MR作业后结果的存放路径

hadoop fs -rm -r -skipTrash $OUTPUT_PATH  #输出路径如果之前存在  先删除否则会报错

hadoop jar $STREAM_JAR_PATH -input $INPUT_FILE_PATH -output $OUTPUT_PATH -mapper "/root/hadoop/env/py3/bin/python mapper.py" -reducer "/root/hadoop/env/py3/bin/python reducer.py" -file ./mapper.py -file ./reducer.py
