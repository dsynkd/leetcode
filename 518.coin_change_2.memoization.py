class Solution:
	def change(self, amount: int, coins: list[int]) -> int:
		self.memo = dict()
		
		def dfs(i, rem) -> int:
			if rem == 0:
				return 1
			if i == len(coins):
				return 0

			if (i, rem) in self.memo:
				return self.memo[(i, rem)]			
	
			res = 0
			if coins[i] > rem:
				res = dfs(i+1, rem)
			else:
				res = dfs(i, rem - coins[i]) + dfs(i+1, rem)
			
			self.memo[(i, rem)] = res
			return res	
			
		return dfs(0, amount)