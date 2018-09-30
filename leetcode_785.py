#coding=utf-8
class Solution:
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        visited=[0 for i in range(len(graph))] #访问过的结点标记为1 
        colornodes=[0 for i in range(len(graph))] #store the color of each node,-1/1
        curnode=0 #当前结点
        color=-1 #初始颜色为-1
        bfslist=[] #bfs队列

        while sum(visited)!=len(graph):
            if len(bfslist)==0: #bfs队列为空
                i=visited.index(0) #未访问过的结点
                visited[i]=1 #标记已访问
                colornodes[i]=color #染色
                bfslist.append(i) #加到bfs队列中
            else:
                curnode=bfslist.pop(0) #pop第一个元素
                color = colornodes[curnode]*-1# 切换染色颜色
                for i in graph[curnode]:
                    if visited[i]==0: #处理未访问过的结点
                        visited[i]=1 #标记已访问
                        colornodes[i]=color #染色
                        bfslist.append(i) #加到bfs队列中

        for i in range(len(graph)):
            for j in range(len(graph[i])):
                if colornodes[i]==colornodes[graph[i][j]]:
                    return False

        return True


#g= [[1,3], [0,2], [1,3], [0,2]]
#g=[[1,2,3], [0,2], [0,1,3], [0,2],]
g=[[4,5],[4,6],[5,7],[6,7],[0,1],[0,2],[1,3],[2,3]]
a=Solution().isBipartite(g)
print(a)