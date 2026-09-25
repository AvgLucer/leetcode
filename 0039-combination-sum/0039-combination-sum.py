class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []

        def bt(i,total,path):
            if total == target:
                res.append(path[:])
                return
            
            if total > target:
                return

            for j in range(i,len(candidates)):
                path.append(candidates[j])
                bt(j,total + candidates[j] , path )
                path.pop()
        
        bt(0,0,[])
        return res
        