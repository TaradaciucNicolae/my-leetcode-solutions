class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        graph=[[] for _ in range(n+1)] # facem asa pt ca drumurile incep de la 1, nu de la 0

        for a,b,dist in roads:
            graph[a].append((b,dist))
            graph[b].append((a,dist))



        print(graph)


        stack = [] # ca sa incercam si abordarea DFS
        stack.append(1)

        visited = set([1])

        min_score = float("inf")
        

        while stack:

            city = stack.pop()

            for next_city, distance in graph[city]:

                min_score = min(min_score, distance)

                if next_city not in visited:
                    visited.add(next_city)
                    stack.append(next_city)



        return min_score
