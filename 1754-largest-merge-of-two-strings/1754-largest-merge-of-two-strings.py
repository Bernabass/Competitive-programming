class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        arr1 = list(word1)
        arr2 = list(word2)
        n, m = len(arr1), len(arr2)
        res, ans = [], []
        first = second = 0

        if n < m:
            arr1.extend(["@"]*(m-n))
        else:
            arr2.extend(["@"]*(n-m))
        arr1.append("@")
        arr2.append("@")
        
        new_len  = len(arr1)
        while first < new_len and second < new_len:
            if arr1[first] > arr2[second]:
                res.append(arr1[first])
                first += 1
            elif arr1[first] < arr2[second]:
                res.append(arr2[second])
                second += 1
                
            else:
                if arr1[first:] >= arr2[second:]:
                    res.append(arr1[first])
                    first += 1
                else:
                    res.append(arr2[second])
                    second += 1
        for num in res:
            if num == "@":
                break
            ans.append(num)

        return "".join(map(str,ans))