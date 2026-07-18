class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        # preprocesarea
        pairs = sorted((nums[i], i) for i in range(n))

        sorted_nums = [value for value, index in pairs]

        pos = [0] * n
        for sorted_index, (value, original_index) in enumerate(pairs):
            pos[original_index] = sorted_index



        component = [0] * n

        for i in range(1, n):
            if sorted_nums[i] - sorted_nums[i - 1] > maxDiff:
                component[i] = component[i - 1] + 1
            else:
                component[i] = component[i - 1]


        #
        farthest = [0] * n
        r = 0

        for l in range(n):
            while r + 1 < n and sorted_nums[r + 1] - sorted_nums[l] <= maxDiff:
                r += 1

            farthest[l] = r

        #
        LOG = n.bit_length()

        jump = [[0] * n for _ in range(LOG)]

        jump[0] = farthest[:]

        for k in range(1, LOG):
            for i in range(n):
                jump[k][i] = jump[k - 1][jump[k - 1][i]]

        #
        results = []

        for u, v in queries:
            a = pos[u]
            b = pos[v]

            if a == b:
                results.append(0)
                continue

            if a > b:
                a, b = b, a

            if component[a] != component[b]:
                results.append(-1)
                continue

            cur = a
            steps = 0

            for k in range(LOG - 1, -1, -1):
                if jump[k][cur] < b:
                    cur = jump[k][cur]
                    steps += 1 << k

            results.append(steps + 1)

        return results
