class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost)>sum(gas):
            return -1
        n=len(gas)
        st=0
        tank=0
        for i in range(n):
            if tank<0:
                st=i
                tank=0
            tank+=gas[i]-cost[i]
        return st