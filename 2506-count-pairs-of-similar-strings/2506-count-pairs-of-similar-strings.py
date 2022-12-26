class Solution:
    def similarPairs(self, words: List[str]) -> int:
        for i in range(len(words)):
            temp  = (list(set(list(words[i]))))
            temp.sort()
            temp = "".join(temp)
            words[i] = temp
        uniques = Counter(words)
        total = 0
        for j in uniques:
            total += math.comb(uniques[j],2)
        return total