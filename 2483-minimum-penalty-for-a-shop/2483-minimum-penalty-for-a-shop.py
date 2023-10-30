class Solution:
    def bestClosingTime(self, customers: str) -> int:
        best_score = score = 0
        closing_time = -1
        
        for hour, came in enumerate(customers):
            score += 1 if came == 'Y' else -1
            
            if score > best_score:
                best_score = score
                closing_time = hour
        
        return closing_time + 1        