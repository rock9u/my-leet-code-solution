from collections import deque 
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        dest = len(graph)-1
        queue =deque([(graph[0],[0])])
        while len(queue)!=0:     
            start,path = queue.popleft()
            for i in start:
                if dest == i:
                     result.append(path+[dest])
                else:
                    queue.append((graph[i],path+[i]))
        return result