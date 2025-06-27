from typing import List

class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        # Juntamos cada semente com seu tempo de plantio e crescimento
        seeds = list(zip(growTime, plantTime))
        
        # Ordenamos decrescentemente pelo growTime
        seeds.sort(reverse=True)
        
        current_day = 0
        max_bloom = 0
        for g, p in seeds:
            current_day += p  # Plantamos essa semente
            max_bloom = max(max_bloom, current_day + g)  # Calculamos o florescimento
        
        return max_bloom
