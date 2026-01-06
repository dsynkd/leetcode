from collections import defaultdict, deque

class Solution:
    def alienOrder(self, words: list[str]) -> str:
        adj = defaultdict(set)
        alphabet = set(words[0])

        # Construct a list of vertices (alphabet) and an adjacency list
        for i in range(1, len(words)):
            for c in words[i]:
                alphabet.add(c)
            j = 0
            m = min(len(words[i-1]), len(words[i]))
            while j < m and words[i][j] == words[i-1][j]:
                j += 1
            # edge case where a longer word with identical prefix characters comes first
            if j == m and j < len(words[i-1]):
                return ''
            if j < m:
                adj[words[i-1][j]].add(words[i][j])

        # Construct in-degrees
        in_degree = defaultdict(int)
        for k,nodes in adj.items():
            for node in nodes:
                in_degree[node] += 1

        # Kahn's algorithm 
        q = deque()
        for c in alphabet:
            if c not in in_degree:
                q.append(c)
    
        res = []
        while q:
            node = q.popleft()
            res.append(node)
            for v in adj[node]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    q.append(v)

        return ''.join(res) if len(res) == len(alphabet) else ''
