
fr_info = {

    'Summer': ['John', 'Justin', 'Mike'],

    'John':   ['Summer', 'Justin'],

    'Justin': ['John', 'Summer', 'Mike', 'May'],

    'Mike':   ['Summer', 'Justin'],

    'May':    ['Justin', 'Kim'],

    'Kim':    ['May'],

    'Tom':    ['Jerry'],

    'Jerry':  ['Tom'],

}



def dfs_friends(g, start):
    done = set()       # 1. 이미 방문한 사람을 기록할 '집합' (BFS와 동일)
    order = []         # 방문 순서를 저장할 리스트

    def _dfs(p):
        done.add(p)      # 2. 현재 사람(p)을 '방문 기록'에 추가
        order.append(p)     # 3. 현재 사람(p)을 '방문 순서' 리스트에 추가
        
        for x in g[p]:           # 내 친구(이웃)들을 하나씩 확인
            if x not in done :  # 4. 그 친구가 아직 '방문 기록'에 없다면
                _dfs(x)        # 5. '자기 자신(_dfs)'을 호출해서 더 깊이 이동!

    _dfs(start)    # 6. '시작점(start)'부터 탐색을 시작합니다.
    return order

print("=== DFS: Summer의 모든 친구 ===")

result = dfs_friends(fr_info, 'Summer')

print(result)

print()

print("=== DFS: Jerry의 모든 친구 ===")

result = dfs_friends(fr_info, 'Jerry')

print(result)
