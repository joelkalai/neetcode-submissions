class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for i, x in edges:
            adj[i].append(x)
            adj[x].append(i)
        curr = 0
        visited = set()
        for i in range(n):
            print(i)
            if i in visited:
                continue 
            visited.add(i)
            stk = [] 
            stk.append(i)
            while stk:
                node = stk.pop() 
                for n in adj[node]:
                    if n not in visited:
                        stk.append(n)
                        visited.add(n)
            curr += 1
        return curr
