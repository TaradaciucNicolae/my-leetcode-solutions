class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        v2 = [0,0,1,0,2,0,1,0,3,0]
        v3 = [0,0,0,1,0,0,1,0,0,2]

        tt = t
        a = b = c = d = 0
        while tt % 2 == 0:
            tt //= 2; a += 1
        while tt % 3 == 0:
            tt //= 3; b += 1
        while tt % 5 == 0:
            tt //= 5; c += 1
        while tt % 7 == 0:
            tt //= 7; d += 1
        if tt != 1:
            return "-1"

        minCnt = [[0] * (b + 1) for _ in range(a + 1)]
        for i in range(a + 1):
            for j in range(b + 1):
                if i == 0 and j == 0:
                    continue
                best = float('inf')
                for x in range(2, 10):
                    if x == 5 or x == 7:
                        continue
                    ni = max(0, i - v2[x])
                    nj = max(0, j - v3[x])
                    if ni == i and nj == j:
                        continue
                    best = min(best, 1 + minCnt[ni][nj])
                minCnt[i][j] = best

        def feasible(P, ra, rb, rc, rd):
            ra, rb, rc, rd = max(0, ra), max(0, rb), max(0, rc), max(0, rd)
            need = rc + rd
            if P < need:
                return False
            return minCnt[ra][rb] <= P - need

        def buildSuffix(length, ra, rb, rc, rd):
            s = ['1'] * length
            for pos in range(length):
                remain = length - pos - 1
                for x in range(1, 10):
                    na = max(0, ra - v2[x])
                    nb = max(0, rb - v3[x])
                    nc = max(0, rc - (1 if x == 5 else 0))
                    nd = max(0, rd - (1 if x == 7 else 0))
                    if feasible(remain, na, nb, nc, nd):
                        s[pos] = str(x)
                        ra, rb, rc, rd = na, nb, nc, nd
                        break
            return ''.join(s)

        L = len(num)
        pV2 = [0] * (L + 1)
        pV3 = [0] * (L + 1)
        pC5 = [0] * (L + 1)
        pC7 = [0] * (L + 1)
        first_zero = L
        for i in range(L):
            dg = int(num[i])
            pV2[i+1] = pV2[i] + v2[dg]
            pV3[i+1] = pV3[i] + v3[dg]
            pC5[i+1] = pC5[i] + (1 if dg == 5 else 0)
            pC7[i+1] = pC7[i] + (1 if dg == 7 else 0)
            if dg == 0 and first_zero == L:
                first_zero = i

        if first_zero == L and pV2[L] >= a and pV3[L] >= b and pC5[L] >= c and pC7[L] >= d:
            return num

        top = min(first_zero, L - 1)
        for i in range(top, -1, -1):
            lowDigit = (int(num[i]) + 1) if i < first_zero else 1
            for x in range(lowDigit, 10):
                pa = pV2[i] + v2[x]
                pb = pV3[i] + v3[x]
                pc = pC5[i] + (1 if x == 5 else 0)
                pd = pC7[i] + (1 if x == 7 else 0)
                ra, rb, rc, rd = a - pa, b - pb, c - pc, d - pd
                suffixLen = L - i - 1
                if feasible(suffixLen, ra, rb, rc, rd):
                    prefix = num[:i]
                    suffix = buildSuffix(suffixLen, max(0, ra), max(0, rb), max(0, rc), max(0, rd))
                    return prefix + str(x) + suffix

        Lmin = c + d + minCnt[a][b]
        newLen = max(L + 1, Lmin)
        return buildSuffix(newLen, a, b, c, d)
