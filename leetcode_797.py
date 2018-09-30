#coding=utf-8
class Solution:
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        def dfs(cur, des, path, visited):
            if cur==des: #到达目标点
                result.append(path)
            elif len(graph[cur])!=0: #未到达目标点，且cur点出度不为0，进行递归
                for each in graph[cur]: #对每个出度进行递归
                    if visited[each]==0:
                        cp_path=path.copy() #复制临时路径
                        cp_path.append(each) #添加结点
                        cp_visited=visited.copy() #复制临时访问列表
                        cp_visited[each]=1 #标记结点
                        dfs(each,des,cp_path,cp_visited)
        result=[]
        visited=[0 for i in range(len(graph))]
        visited[0]=1
        dfs(0,len(graph)-1,[0],visited)
        return result

#g=[[1,2], [3], [3], []]
g=[[1,2,3],[0,2,3],[0,1,3],[0,1,2]]
a=Solution().allPathsSourceTarget(g);
print(a)
