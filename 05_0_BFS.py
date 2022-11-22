from collections import deque

def bfs(graph, start, visited):
    #큐 구현을 위한 deque 라이브러리 사용
    queue = deque([start])
    #현재 방문한 노드에 대한 방문 처리
    visited[start] = True
    #큐가 빌 때까지 반복
    while queue:
        v=queue.popleft()
        print(v, end=' ')
        #해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]: 
                queue.append(i)
                visited[i] = True

graph=[
    []
    , [2, 3, 8]
    , [1, 7]
    , [1, 4, 5]
    , [3, 5]
    , [3, 4]
    , [7]
    , [2, 6]
    , [1, 7]
]

visied = [False] * 9

bfs(graph, 1, visied)