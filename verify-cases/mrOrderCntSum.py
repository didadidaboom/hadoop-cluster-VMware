from mrjob.job import MRJob
import os
import sys

# name table
# user_id user_name
# 01  user1
# 02  user2
# 03  user3

#order table
# user_id order_id order_price
# 01  01  80
# 01  02  90
# 02  03  82
# 02  04  95

class UserOrderJoin(MRJob):
	SORT_VALUES = True
	def mapper(self,_,line):
		fields = line.strip().split()
		if len(fields) == 2:
			# user data
			source = 'A'
			user_id = fields[0]
			user_name = fields[1]
			yield user_id,[source,user_name]  #01,[A,user1]
		elif len(fields) == 3:
			# order data
			source = 'B'
			user_id = fields[0]
			order_id = fields[1]
			price = fields[2]
			yield user_id,[source,order_id,price]
		else:
			pass
	def reducer(self,user_id,values):
		'''
		统计每个用户的订单数量和累计消费金额
		:param user_id
		:param values
		:return:
			"01:user1" [order_cnt,order_sum]
		'''
		values = [v for v in values]
		user_name = None
		order_cnt = 0
		order_sum = 0
		if len(values) > 1:
			for v in values:
				if len(v) == 2:
					user_name = v[1]
				elif len(v) == 3:
					order_cnt += 1
					order_sum += int(v[2])
			yield ":".join([user_id,user_name]),(order_cnt,order_sum)


if __name__=="__main__":
	UserOrderJoin.run()
