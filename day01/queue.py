# enqueue : 뒤에 데이터 추가
# dequeue : 앞에 데이터를 꺼냄
'''
활용예시
- 프린터 출력 대기열
- ROS 토픽 메시지 버퍼
- BFS
'''

from collections import deque

queue = deque() # 앞의 데이터를 꺼냄
queue.append('A') # enqueue A -> deque (['A']
queue.append('B') # enqueue B -> deque (['A','B']
queue.append('C') # enqueue C -> deque (['A','B','C']
print(queue)
print(queue.popleft()) # -> 'A' (가장 먼저 넣은 A가 먼저나옴)
print(queue)
print(queue.popleft()) # -> 'B'
print(queue)
