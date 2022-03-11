from mrjob.job import MRJob,MRStep
import heapq

class TopN(MRJob):
	def mapper(self,key,line):
		if line.strip()!="":
			for word in line.split():
				yield word,1
	def combiner(self,word,counts):
		yield word,sum(counts)
	def reducer_sum(self,word,counts):
		yield None,(sum(counts),word)
	def top_n_reducer(self,_,word_counts):
		for count,word in heapq.nlargest(2,word_counts):
			yield word,count
	def steps(self):
		return[
			MRStep(mapper=self.mapper,combiner=self.combiner,reducer=self.reducer_sum),MRStep(reducer=self.top_n_reducer)
			]
if __name__=="__main__":
	TopN.run()

