from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Garante que nums1 seja o menor dos dois arrays
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2

        left, right = 0, m

        while True:
            i = (left + right) // 2  # posição de corte em nums1
            j = half - i             # posição de corte em nums2

            # Valores à esquerda e à direita das partições
            Aleft = nums1[i - 1] if i > 0 else float("-infinity")
            Aright = nums1[i] if i < m else float("infinity")
            Bleft = nums2[j - 1] if j > 0 else float("-infinity")
            Bright = nums2[j] if j < n else float("infinity")

            # Verifica se a partição está correta
            if Aleft <= Bright and Bleft <= Aright:
                # Se o total de elementos for ímpar
                if total % 2:
                    return min(Aright, Bright)
                # Se for par, média dos dois do meio
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                # Vai mais para a esquerda no nums1
                right = i - 1
            else:
                # Vai mais para a direita no nums1
                left = i + 1
