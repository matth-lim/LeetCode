class Solution:
    def average(self, salary):
        """
        type salary: List[int]
        rtype: float
        """
        sum = 0
        for x in salary:
            sum += x
        return (sum - max(salary) - min(salary)) / (len(salary) - 2)