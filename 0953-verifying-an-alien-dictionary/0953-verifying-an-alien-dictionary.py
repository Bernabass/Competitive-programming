class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alphabet = dict(zip(order,range(26)))
        alphabet[""] = -1
        for i in range(1,len(words)):
            first = list(words[i-1])
            second = list(words[i])
            n1 , n2 = len(first) , len(second)
            if n1 > n2:
                second.extend((n1 - n2)*[""])
            else:
                first.extend((n2 - n1)*[""])
            count = 0
            while count < len(first):
                if alphabet[second[count]] > alphabet[first[count]]:
                    break
                elif alphabet[second[count]] < alphabet[first[count]]:
                    return False
                count += 1
        return True    