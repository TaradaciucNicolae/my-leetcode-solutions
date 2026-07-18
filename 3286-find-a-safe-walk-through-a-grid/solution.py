import heapq
from typing import List

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        
        m = len(grid)
        n = len(grid[0])

        dist = [[float("inf")] * n for _ in range(m)] # refac matricea cu "inf"
        # matricea dist are rolul sa pun in ea distanta parcursa pana la ea, adica in cazul nostru minimul health pierdut pana acolo

        dist[0][0]= grid[0][0] # si setez primul din dist cu primul din grid

        heap = [] # il folosim pt ca el scoate mereu minimul
                  # in timp de deque scoate din spate sau din fata

        # heap il vom popula cu tuple-uri de forma (cost, row, col)
        # costul e primul pt ca heap sorteaza dupa primul element, de aia
        # si vom adauga si punctul de start in heap

        movements = [
            (0, 1),   # dreapta
            (0, -1),  # stânga
            (1, 0),   # jos
            (-1, 0)   # sus
        ]

        heapq.heappush(heap, (dist[0][0], 0, 0))

        while heap:
            
            
            (cost, row, col) = heapq.heappop(heap)

            for di, dj in movements:
                new_i = di + row
                new_j = dj + col

                if new_i < 0 or new_i >= m or new_j < 0 or new_j >= n:
                    continue


                cost_nou=  cost + grid[new_i][new_j]

                if cost_nou < dist[new_i][new_j]: # nu am pus <= ca sa nu il facem sa se intoarca inapoi in cazul cand inainte era acelasi cost ( exemplu cu o coloana de 0)
                    dist[new_i][new_j] = cost_nou

                    heapq.heappush(heap, (cost_nou, new_i, new_j))

        cost_final = dist[m - 1][n - 1]
        
        if cost_final < health:
            return True
        else:
            return False
