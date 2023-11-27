import pickle

class NPC:
    def __init__(self, x, y, name):
        self.x, self.y, self.name = x, y, name

with open('npc.pickle', 'rb') as f:
    group = pickle.load(f)

for o in group:
    print(o.name, o.x, o.y)

# __dict__ : 객체가 갖고 있는 모든 속성.
# pickle로 필요한 속성만 저장가능. set state, get state 내장함수를 이용해서 가능
