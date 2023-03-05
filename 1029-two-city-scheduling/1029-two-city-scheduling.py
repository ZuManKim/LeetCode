class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        cost_city_a = [i for i, j in costs]
        diff_cost = [j-i for i, j in costs]
        diff_cost.sort()
        lowest_half_diff = sum(diff_cost[:len(costs)//2])
        return sum(cost_city_a) + lowest_half_diff
        