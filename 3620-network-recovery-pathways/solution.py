from typing import List
import heapq


class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:

        n = len(online) # nr de noduri

        # 1. Construim graful

        graph = [[] for _ in range(n)] # o lista x de liste xi si fiecare lista xi va fi un edge/muchie

        highest_edge_cost = 0

        for from_node, to_node, edge_cost in edges:
            graph[from_node].append((to_node, edge_cost)) # punem acele liste si practic se va sti ca de la 0 putem merge si catre un un not si catre alt nod pt ca el poate arata ceva genul 
            #  graph = [
            #  [(1, 5), (2, 3)],  # din nodul 0 poți merge la 1 cu cost 5 și la 2 cu cost 3
            #   [],               # din nodul 1 nu pleacă nicio muchie
            #  [(3, 4)],          # din nodul 2 poți merge la 3 cu cost 4
            #   }
            highest_edge_cost = max(highest_edge_cost, edge_cost) # il vom patra pt ca va fi limita de right in binary search


        # 2. DIJKSTRA
        #
        # Aici practic cautam un drum in care : fiecare edge are cost >= candidate_score
        # si
        # in care suma tuturor muchiilor de pe drum este  <=k
        # sau altfel explicat
        # candidate_score = limita minimă acceptată pentru fiecare muchie
        # k = limita maximă acceptată pentru suma totală a drumului
        
        def is_score_possible(candidate_score: int) -> bool:
            INF = 10 ** 30

            # minimum_total_cost_to_reach[node] = cel mai mic cost total găsit până acum ca să ajungem la node
            minimum_total_cost_to_reach = [INF] * n
            minimum_total_cost_to_reach[0] = 0

            # heap-ul conține perechi:
            # (cost_total_până_acum, nod_curent)
            min_heap = [(0, 0)]

            while min_heap:
                current_total_cost, current_node = heapq.heappop(min_heap)

                # Dacă valoarea scoasa din heap nu e cea mai buna valoare cunoscuta pt nodul curent, atunci o ignoram
                if current_total_cost != minimum_total_cost_to_reach[current_node]:
                    continue

                # Dacă am ajuns la destinație, verificăm dacă drumul este în buget.
                # Dijkstra ne garantează că acesta este cel mai ieftin drum găsit către destinație.
                if current_node == n - 1:
                    return current_total_cost <= k

                # Încercăm toate muchiile care pleacă din current_node
                for next_node, edge_cost in graph[current_node]:

                    # Pentru ca scorul path-ului să fie cel puțin candidate_score,
                    # fiecare muchie folosită trebuie să aibă cost >= candidate_score.
                    if edge_cost < candidate_score:
                        continue

                    # Nu avem voie să trecem prin noduri offline.
                    # Nodurile 0 și n - 1 sunt mereu online conform problemei.
                    if not online[next_node]:
                        continue

                    new_total_cost = current_total_cost + edge_cost

                    # Relaxare Dijkstra:
                    # dacă am găsit un drum mai ieftin către next_node,
                    # îl salvăm și îl punem în heap.
                    if new_total_cost < minimum_total_cost_to_reach[next_node]:
                        minimum_total_cost_to_reach[next_node] = new_total_cost
                        heapq.heappush(min_heap, (new_total_cost, next_node))

            # Dacă heap-ul s-a golit și nu am ajuns la n - 1,
            # atunci nu există drum valid pentru acest candidate_score.
            return False


        # 3. BINARY SEARCH ON ANSWER

        # Căutăm cel mai mare scor posibil.
        #
        # Scorul unui path = cea mai mică muchie de pe acel path.
        #
        # Dacă un scor X este posibil, încercăm să vedem dacă putem obține un scor mai mare.
        #
        lowest_candidate_score = 0
        highest_candidate_score = highest_edge_cost
        best_valid_score = -1

        while lowest_candidate_score <= highest_candidate_score:
            candidate_score = (lowest_candidate_score + highest_candidate_score) // 2

            if is_score_possible(candidate_score):
                # candidate_score merge.
                # Îl salvăm și încercăm unul mai mare.
                best_valid_score = candidate_score
                lowest_candidate_score = candidate_score + 1
            else:
                # candidate_score este prea mare.
                # Trebuie să încercăm scoruri mai mici.
                highest_candidate_score = candidate_score - 1

        return best_valid_score
