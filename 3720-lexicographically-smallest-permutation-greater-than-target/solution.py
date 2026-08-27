class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        
        list_s = sorted(list(s))
        candidates = []

        for i in range(len(target)):
            remaining = list_s[:]
            
            valid_prefix = True
            for j in range(i):
                if target[j] in remaining:
                    remaining.remove(target[j])
                else:
                    # prefix cannot be formed
                    valid_prefix = False
                    break
            
            if not valid_prefix:
                continue

            # at position i, find the first character strictly greater than target[i]
            deviation = None
            for ch in remaining:
                if ch > target[i]:
                    deviation = ch
                    remaining.remove(ch)
                    break
            
            if deviation is None:
                continue

            # build the candidate
            prefix = target[0:i]
            rest = "".join(remaining)  # remaining is already sorted
            candidate = prefix + deviation + rest
            candidates.append(candidate)

        if not candidates:
            return ""
        return sorted(candidates)[0]
