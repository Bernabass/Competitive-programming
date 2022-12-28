class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        result = []
        occurence = defaultdict(list)
        for i in range(len(paths)):
            paths[i] = paths[i].split()
            directory , files = paths[i][0] , paths[i][1:]
      
            for file in files:
                temp = file.split("(")
                occurence[temp[1]].append("/".join([directory,temp[0]]))
        
        for duplicates in occurence.values():
            if len(duplicates) > 1:
                result.append(duplicates)
            
        return result