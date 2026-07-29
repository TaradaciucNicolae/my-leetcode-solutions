class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        LIMIT = k  # nu ne intereseaza valori mai mari decat k

        # 1. Numaram literele
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord("a")] += 1

        # 2. Construim frecventele pentru prima jumatate
        half_count = [0] * 26
        middle = ""

        for i in range(26):
            half_count[i] = freq[i] // 2

            if freq[i] % 2 == 1:
                middle = chr(ord("a") + i)

        # Calculeaza C(n, r), dar se opreste daca devine prea mare.
        # Exemplu: C(5, 2) = 10
        def combination_limited(n, r, limit):
            if r > n:
                return 0

            r = min(r, n - r)
            answer = 1

            for i in range(1, r + 1):
                answer = answer * (n - r + i) // i

                if answer > limit:
                    return limit + 1

            return answer

        # Cate permutari distincte putem face cu literele ramase?
        def count_permutations(counts, limit):
            total_letters = sum(counts)
            ways = 1

            for cnt in counts:
                if cnt == 0:
                    continue

                # Alegem pozitiile pentru aceasta litera.
                # Daca deja avem multe ways, limitam calculul.
                max_needed = limit // ways

                if max_needed == 0:
                    return limit + 1

                choose = combination_limited(total_letters, cnt, max_needed)

                if choose > max_needed:
                    return limit + 1

                ways *= choose
                total_letters -= cnt

                if ways > limit:
                    return limit + 1

            return ways

        # 3. Verificam daca exista macar k palindromuri distincte
        total = count_permutations(half_count, LIMIT)

        if total < k:
            return ""

        # 4. Construim prima jumatate a raspunsului
        left_half = []
        half_length = sum(half_count)

        for _ in range(half_length):

            # Incercam literele in ordine alfabetica:
            # a, b, c, ..., z
            for i in range(26):
                if half_count[i] == 0:
                    continue

                # Presupunem ca punem aceasta litera acum
                half_count[i] -= 1

                # Vedem cate palindromuri putem face dupa aceasta alegere
                ways = count_permutations(half_count, k)

                if ways >= k:
                    # Litera aceasta este corecta pentru pozitia curenta
                    left_half.append(chr(ord("a") + i))
                    break
                else:
                    # Al k-lea raspuns nu incepe cu aceasta litera.
                    # Sarim peste toate variantele care incep asa.
                    k -= ways
                    half_count[i] += 1

        left_half = "".join(left_half)

        # 5. Palindrome = stanga + mijloc + inversul stangii
        return left_half + middle + left_half[::-1]
