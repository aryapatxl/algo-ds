class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      # fixed size array!

      hashy = {}

      for string in strs: # O(n) where n = # of strings
        key = [0] * 26 # O(26)
        for letter in string: # O(m) where = len of longest string
            key[ord(letter)-ord('a')] += 1
        if tuple(key) not in hashy:
            hashy[tuple(key)] = [string]
        else: hashy[tuple(key)].append(string)
      return list(hashy.values())
    

