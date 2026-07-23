class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        nr_of_prov = 0
        nr_of_cities = len(isConnected)

        visited_cities = [False]* nr_of_cities

        def dfs(i):
            visited_cities[i] = True

            for j in range(nr_of_cities):
                if isConnected[i][j] == 1 and visited_cities[j] == False:
                    dfs(j)

        

        for i in range(nr_of_cities):
            if visited_cities[i] == False:
                nr_of_prov += 1
                dfs(i)


        return nr_of_prov
