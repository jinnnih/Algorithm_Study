# 친구 관계 그래프 (실습 2에서 만든 것과 동일)
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

def print_all_friends(g, start):
    qu = []       # 큐 생성
    done = set()  # 방문 기록용 집합

    # 1. (이름, 친밀도)를 튜플로 묶어서 큐에 추가 (시작점은 0촌)
    qu.append((start, 0))  
    done.add(start)

    while qu:
        # 2. 큐의 맨 앞에서 (이름, 친밀도)를 함께 꺼냄
        p, d = qu.pop(0)  
        print(p, d)  # 이름과 친밀도 출력

        for x in g[p]:
            if x not in done:
                # 3. 친구(x)는 나(p)보다 한 단계 더 멀리 있으므로 d + 1
                qu.append((x, d + 1)) 
                done.add(x)

print("=== Summer와의 친밀도 ===")
print_all_friends(fr_info, 'Summer')