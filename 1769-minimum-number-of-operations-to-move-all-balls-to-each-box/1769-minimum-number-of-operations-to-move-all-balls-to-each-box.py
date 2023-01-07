class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        right = boxes[1:].count("1")
        left = int(boxes[0])
        res = [0] * len(boxes)
        for idx,val in enumerate(boxes):
            if val == "1":
                res[0] += idx
      
        boxes = boxes[1:]
        for idx,val in enumerate(boxes,1):
            res[idx] += res[idx-1] - (right - left)
            if val == "1":
                left += 1
                right -= 1
                
        return res