import heapq

# 격자 맵 — 숫자 = 이동 비용, -1 = 벽(이동 불가)
grid = [
    [1,  1,  1,  3,  1],
    [1, -1, -1,  3,  1],
    [1, -1,  5,  3,  1],
    [1,  1,  1,  1,  1],
    [1,  1,  1,  1,  1],
]

start = (0, 0)    # 출발점
goal = (4, 4)     # 도착점

# 상하좌우 이동 방향
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def grid_dijkstra(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0])
    
    # 모든 칸의 거리를 무한대로 초기화
    distances = [[float('inf')] * cols for _ in range(rows)]
    distances[start[0]][start[1]] = 0   # 시작 칸은 비용 0
    
    # 경로 추적용: 각 칸에 "어디서 왔는지" 기록
    parent = [[None] * cols for _ in range(rows)]
    
    # 우선순위 큐: (비용, 행, 열)
    heap = []
    heapq.heappush(heap, (0, start[0], start[1]))
    visited = set()

    while heap:
        # [수정] heappush가 아니라 heappop으로 가장 작은 비용을 꺼내야 합니다.
        cost, r, c = heapq.heappop(heap) 

        if (r, c) in visited:
            continue
        visited.add((r, c))

        # [수정] 도착점에 도달하면 종료 (r, c == goal)
        if (r, c) == goal:
            break

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            # 빈칸 1: 범위 체크 + 벽 체크 (grid[nr][nc] != -1)
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != -1:
                
                # 빈칸 2: 현재 비용 + 이동할 칸의 비용 (cost + grid[nr][nc])
                new_cost = cost + grid[nr][nc]
                
                if new_cost < distances[nr][nc]:
                    distances[nr][nc] = new_cost
                    # 빈칸 3: 어디서 왔는지 기록 (r, c)
                    parent[nr][nc] = (r, c)
                    heapq.heappush(heap, (new_cost, nr, nc))

    # 경로 복원: goal에서 start까지 거꾸로 추적
    path = []
    current = goal
    
    # 만약 도착점에 도달할 수 없는 경우 빈 리스트 반환
    if distances[goal[0]][goal[1]] == float('inf'):
        return float('inf'), []

    while current is not None:
        path.append(current)
        current = parent[current[0]][current[1]]
    
    path.reverse()
    return distances[goal[0]][goal[1]], path

# 실행
total_cost, path = grid_dijkstra(grid, start, goal)

print(f"최소 비용: {total_cost}")
print(f"경로: {path}")

# 격자 맵에 경로 표시
print("\n=== 경로 시각화 ===")
for r in range(len(grid)):
    row_str = ""
    for c in range(len(grid[0])):
        if (r, c) == start:
            row_str += " S "
        elif (r, c) == goal:
            row_str += " G "
        elif (r, c) in path:
            row_str += " * "
        elif grid[r][c] == -1:
            row_str += " ■ "
        else:
            row_str += f" {grid[r][c]} "
    print(row_str)