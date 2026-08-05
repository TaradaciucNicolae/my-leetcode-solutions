class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        nodes = defaultdict(list)
        for a, b in invocations:
            nodes[a].append(b)

        #  reachable from k
        visited = {k}
        stack = [k]
        while stack:
            node = stack.pop()
            for nxt in nodes[node]:
                if nxt not in visited:
                    visited.add(nxt)
                    stack.append(nxt)

        # check if any node outside the group invokes into the group
        removable = True
        for a, b in invocations:
            if b in visited and a not in visited:
                removable = False
                break

        output=[]    
        
            
        # if it can't be removed -> return all nodes unchanged
        if not removable:
            output = list(range(0,n))
            return output
        else: 
            
            #  return only the non-suspicious methods
            for i in range(0,n):
                if i not in visited:
                    output.append(i)
            
            return output
