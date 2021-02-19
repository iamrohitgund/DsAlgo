#Two Sum
def twoNumberSum(array, targetSum):
	map = {}
	for num in array:
		potentialMatch = targetSum - num
		if potentialMatch in map:
			return [potentialMatch, num]
		else:
			map[num] = True
	return []

#Time and Space O(n)
