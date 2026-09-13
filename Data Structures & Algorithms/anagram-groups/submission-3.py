class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]

        anagramcount = {}
        for word in strs:
            arr = [0]*26
            for letter in word:
                arr[ord(letter) - ord('a')] += 1
            count = tuple(arr)

            if count in anagramcount:
                anagramcount[count] += [word]
            else:
                anagramcount[count] = [word]

        return [x for x in anagramcount.values()]
