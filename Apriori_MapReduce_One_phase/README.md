# Implement  One Phase Algorithm on Python mrjob in MapReduce framework

## Introduction 

Frequent Itemset Mining in MapReduce framework 

One phase is like greed method to generate every subsets in each transcation list

Subset part can see in **subset_example.py**

## Job part

 Only use one job to find frequent itemsets 

### Map part

To generate every subsets in each transcation list and output <itemset,1> 

	Key:Itemset from transcation list
	
	Value:Itemset count 1

### Reduce part

According each Key to sum the value

If value equal or bigger than **Minsupport** output frequent itemsets


