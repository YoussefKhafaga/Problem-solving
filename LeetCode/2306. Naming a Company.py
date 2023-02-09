class Solution(object):
    def distinctNames(self, ideas):
        result = 0
        initial_groups = [set() for _ in range(26)]
        for idea in ideas:
            initial_groups[ord(idea[0]) - ord('a')].add(idea[1:])
        for i in range(25):
            for j in range(i+1, 26):
                num_of_mutual = len(initial_groups[i] & initial_groups[j]) 
                result += 2 * (len(initial_groups[i]) - num_of_mutual) * (len(initial_groups[j]) - num_of_mutual)
        return result