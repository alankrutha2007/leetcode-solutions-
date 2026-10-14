class Solution:
    def average(self, salary: list[int]) -> float:
        n=len(salary)
        Total_sum=sum(salary)-min(salary)-max(salary)
        return Total_sum/(n-2)
