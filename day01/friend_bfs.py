# 친구 관계 그래프

# A와 B가 친구이면, A의 리스트에 B가, B의 리스트에 A가 모두 있어야 합니다.

# 실습 2 빈칸 채우기 예시
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

# 확인: May의 친구 목록 출력
print("May의 친구:", fr_info['May'])


def print_all_friends(g, start):
    qu = []          # 앞으로 처리해야 할 사람들을 저장하는 큐
    done = set()    # 1. 이미 큐에 추가한 사람들을 기록하는 '집합' (중복 방지)

    qu.append(start)     # 2. 자신을 큐에 '추가'하고 시작
    done.add(start)   # 3. 집합에도 '추가'

    while qu  :               # 4. 큐에 처리할 사람이 '남아 있는 동안'
        p = qu.pop(0)        # 5. 큐 맨 '앞'에서 한 명 꺼내기
        print(p)                # 이름 출력

        for x in g[p]:              # 꺼낸 사람의 친구들 중에서
            if x not in done:     # 6. 아직 '집합'에 없는 사람만
                qu.append(x)   # 7. 큐에 '친구 이름' 추가
                done.add(x)    # 8. 집합에도 '친구 이름' 추가

# 실행 코드
print("=== Summer의 모든 친구 ===")
print_all_friends(fr_info, 'Summer')