def print_all_friends_broken(g, start):

    qu = []

    # done 없이 실행 — 무한 반복 발생!

    qu.append(start)

    count = 0

    while qu and count < 20:   # 무한 루프 방지를 위해 20번만 실행

        p = qu.pop(0)

        print(p)

        for x in g[p]:

            qu.append(x)       # 중복 체크 없이 그냥 추가

        count += 1

print("=== done 없이 실행 (20번 제한) ===")

print_all_friends_broken(fr_info, 'Tom')


# 어떤 이름이 계속 반복되나요? Summer, John
# done 집합은 어떤 역할을 하나요? 중복 방지, 방문 기록
# 로봇 경로 탐색에서 done에 해당하는 것은? 방문 지도, 지나온 궤적