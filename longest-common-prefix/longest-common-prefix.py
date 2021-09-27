class Solution:
	def longestCommonPrefix(self, strs: List[str]) -> str:
		smallest = None

		for value in strs:
			if smallest is None:
				smallest = value 
			else:
				if len(value) < len(smallest):
					smallest = value

		prefix = ''
		for i in range(len(smallest)):
			in_all = True
			for item in strs:
				if item[i] != smallest[i]:
					in_all = False

			if in_all:
				prefix += smallest[i]
			else:
				return prefix

		return prefix