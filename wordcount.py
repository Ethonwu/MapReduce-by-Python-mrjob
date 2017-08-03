from mrjob.job import MRJob
class MRWordCount(MRJob):
    def mapper(self, _, line):
        for letter in line:
            for word in letter:
                yield(word, 1)
    def reducer(self, word, counts):
            yield(word, sum(counts))
if __name__ == '__main__':
    MRWordCount.run()
