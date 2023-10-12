# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        N = mountain_arr.length()
        left, right = 0, N - 1
        
        @cache
        def get(idx):
            return mountain_arr.get(idx)
        
        while left <= right:
            mid = (left + right) // 2
            
            if get(mid - 1) > get(mid) > get(mid + 1):
                right = mid

            elif get(mid - 1) < get(mid) < get(mid + 1):
                left = mid

            else:
                peak = mid
                break
    
    
        left, right = 0, peak
        ans = -1

        while left <= right:
            mid = (left + right) // 2

            if get(mid) > target:
                right = mid - 1

            elif get(mid) < target:
                left = mid + 1

            elif mid - 1 > -1 and get(mid - 1) == target:
                right = mid - 1

            else:
                ans = mid
                break

        if ans != -1:
            return ans

        left, right = N - 1, peak + 1
        ans = -1

        while left >= right:
            mid = (left + right) // 2

            if get(mid) > target:
                right = mid + 1

            elif get(mid) < target:
                left = mid - 1

            elif mid + 1 < N and get(mid + 1) == target:
                    right = mid + 1

            else:
                ans = mid
                break

        return ans