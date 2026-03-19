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
queue.append('A') # enqueue A -> deque
queue.append('B') # enqueue B -> deque
queue.append('C') # enqueue C -> deque
print(queue)
print(queue.popleft())
print(queue)
print(queue.popleft())
print(queue)
