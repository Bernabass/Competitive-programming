class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res , next_ = [] , []
        flag = True
        for line in source:
            count = 0 
            while count < len(line):
                check = line[count:count + 2] 
                if flag and check == "/*":
                    flag = False
                    count += 2 
                elif flag and check == "//": 
                    count = len(line)
                elif not flag and check == "*/":
                    flag = True
                    count += 2 
                elif not flag:
                    count += 1 
                else:
                    next_.append(line[count])
                    count += 1 
            if flag and next_:
                res.append("".join(next_))
                next_ = []
        if next_:
            res.append("".join(next_)) 
        return res