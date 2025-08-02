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
        indegree = defaultdict(int)
        for k,nodes in adj.items():
            for node in nodes:
                indegree[node] += 1

        # Kahn's algorithm for topological ordering
        q = deque()
        for c in alphabet:
            if c not in indegree:
                q.append(c)
    
        res = []
        while q:
            node = q.popleft()
            res.append(node)
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        if len(alphabet) != len(res):
            return ''

        return ''.join(res)
