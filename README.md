# MapReduce Job in Python mrjob

## Installation
Using pip or easy_install to download mrjob:
	
	pip install mrjob
	easy_install mrjob

## Run
Local MapReduce

	python wordcount.py example.txt
	
Hadoop MapReduce

	python wordcount.py test.txt -r hadoop \
	--jobconf mapreduce.job.priority=VREY_HIGH \ 
	--jobconf mapreduce.job.maps=2 \
	--jobconf mapreduce.job.reduces=1 \ 
	-o hdfs:///OUTPUT PATH hdfs:///INPUT PATH
## Output
	

