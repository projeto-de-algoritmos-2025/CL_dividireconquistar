from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Inicializa dp com infinito (um valor alto), exceto dp[0] = 0
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        # Para cada valor de 1 até amount, calcula o mínimo de moedas
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        # Se dp[amount] não foi atualizado, é impossível formar o valor
        return dp[amount] if dp[amount] != float('inf') else -1
