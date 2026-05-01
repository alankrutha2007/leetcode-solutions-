from collections import deque
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj=[]
        for _ in range(n):
            adj.append([])
        for u,v in dislikes:
            u-=1
            v-=1
            adj[u].append(v)
            adj[v].append(u)
        color=[-1]*n
        for i in range(n):
            if(color[i]==-1):
                q=deque([i])
                color[i]=0
                while(len(q)>0):
                    node=q.popleft()
                    for adjNode in adj[node]:
                        if(color[adjNode]== -1):
                            color[adjNode]=1-color[node]
                            q.append(adjNode)
                        elif(color[node]==color[adjNode]):
                            return False
        return True
