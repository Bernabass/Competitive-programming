class Solution:
    def average(self, salary: List[int]) -> float:
        total , quantity , maxx , minn = 0 , len(salary) - 2 , max(salary) , min(salary)
        for i in salary:
            if i != maxx and i != minn:
                total += i
        return total/quantity