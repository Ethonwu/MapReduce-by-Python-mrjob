from mrjob.job import MRJob
from mrjob.step import MRStep
import itertools
class MRWordCount(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_oneitemset,
                   reducer=self.reducer_oneitemset)
                ]
    def mapper_oneitemset(self, _, line):
        line = str(line).replace(" ","")
        subsets = []
        for i in range(1,len(line)+1):
            for combo in itertools.combinations(line,i):
                yield(combo,1)
        #yield (subset,1)
    def reducer_oneitemset(self, word, counts):
        minsupport = 2
        support_count = sum(counts)
        if support_count >= minsupport:  
            yield(word, support_count)
if __name__ == '__main__':
    MRWordCount.run()
    
