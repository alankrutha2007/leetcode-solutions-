from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        l=len(graph)
        color=[-1]*l
        for n in range(l):#apply BFS to each node 
            if(color[n]==-1):
                color[n]=1
                q=deque([n])
                while(len(q)>0):
                    node=q.popleft()
                    for i in graph[node]:
                        if(color[i]==-1):
                            color[i]=1-color[node]
                            q.append(i)
                        elif(color[i]!=-1):
                            if(color[node]==color[i]):
                                return False
        return True
