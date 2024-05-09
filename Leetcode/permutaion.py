class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(arr, i , temp):
            if len(arr) == 0:
                res.append(temp.copy())
                return
            for j in range(len(arr)):
                ele = arr[j]
                print("element is ", ele)
                temp.append(ele)
                dfs(arr[0:j]+arr[j+1:], i+1, temp)
                temp.pop()

        dfs(nums, 0, [])
        print(res)
        return res
