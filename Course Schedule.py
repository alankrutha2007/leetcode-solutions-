from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj=[]
        for _ in range(numCourses):
            adj.append([])
        for u,v in prerequisites:
            adj[u].append(v)
        inDegre=[0]*numCourses
        for u,v in prerequisites:
            inDegre[v]+=1
        q=deque([])
        for i in range(0,numCourses):
            if(inDegre[i]==0):
                q.append(i)
        ans=[]
        while(len(q)>0):
            node=q.popleft()
            ans.append(node)
            for adjNode in adj[node]:
                inDegre[adjNode]-=1
                if(inDegre[adjNode]==0):
                    q.append(adjNode)
        if(len(ans)==numCourses):
            return True
        else:
            return False
