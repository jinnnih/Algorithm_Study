import heapq

# 격자 맵: 숫자 = 이동 비용, -1 = 벽(장애물)
grid = [
    [1,  1,  1,  3,  1],
    [1, -1, -1,  3,  1],
    [1, -1,  5,  3,  1],
    [1,  1,  1,  1,  1],
    [1,  1,  1,  1,  1],
]

start = (0, 0)
goal = (4, 4)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 휴리스틱 함수: 맨해튼 거리 (가로 차이 + 세로 차이)
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def grid_astar(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0])
    
    # g_cost: 출발점에서 현재까지의 실제 누적 비용
    g_cost = [[float('inf')] * cols for _ in range(rows)]
    g_cost[start[0]][start[1]] = 0
    
    parent = [[None] * cols for _ in range(rows)]
    
    # 우선순위 큐: (f, 행, 열) -> f = g + h
    heap = []
    # 시작점에서 목표까지의 추정 거리 h 계산
    h = heuristic(start, goal)
    heapq.heappush(heap, (0 + h, start[0], start[1]))
    
    visited = set()
    visit_count = 0  # 탐색한 칸 수 카운트
    
    while heap:
        f, r, c = heapq.heappop(heap)
        
        if (r, c) in visited:
            continue
        visited.add((r, c))
        visit_count += 1
        
        # 도착점 도달 시 종료
        if (r, c) == goal:
            break
            
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            # 격자 범위 내 + 벽이 아님
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != -1:
                new_g = g_cost[r][c] + grid[nr][nc]
                
                if new_g < g_cost[nr][nc]:
                    g_cost[nr][nc] = new_g
                    # h: 현재 이웃(nr, nc)에서 목표(goal)까지의 추정 거리
                    h_val = heuristic((nr, nc), goal)
                    # f = g + h (실제 온 거리 + 남은 예상 거리)
                    f_val = new_g + h_val
                    
                    parent[nr][nc] = (r, c)
                    heapq.heappush(heap, (f_val, nr, nc))
                    
    # 경로 복원
    path = []
    curr = goal
    while curr is not None:
        path.append(curr)
        curr = parent[curr[0]][curr[1]]
    path.reverse()
    
    return g_cost[goal[0]][goal[1]], path, visit_count

# 실행 및 결과 출력
total_cost, path, count = grid_astar(grid, start, goal)

print(f"최소 비용: {total_cost}")
print(f"탐색한 칸 수: {count}")
print(f"경로: {path}")

print("\n=== 경로 시각화 (A*) ===")
for r in range(len(grid)):
    row_str = ""
    for c in range(len(grid[0])):
        if (r, c) == start: row_str += " S "
        elif (r, c) == goal: row_str += " G "
        elif (r, c) in path: row_str += " * "
        elif grid[r][c] == -1: row_str += " ■ "
        else: row_str += f" {grid[r][c]} "
    print(row_str)