# game world 관리 모듈

# game world 표현
# 2개의 layer를 갖는 game world로 구현
# 0번 list-> layer0, 1번 list-> layer1
objects = [[], []]    # 객체들의 리스트

# 월드에 객체를 넣는 함수
def add_object(o, depth=0): #기본 depth는 0. 가장 뒤
    objects[depth].append(o)

# 월드를 업데이트하는, 객체들을 모두 업데이트 하는 함수
def update():
    for layer in objects:
        for o in layer:
            o.update()

# 월드 객체들을 모두 그리기
def render():
    for layer in objects:
        for o in layer:
            o.draw()

def remove_object(o):
    for layer in objects:
        if o in layer:
            layer.remove(o)
            return
    raise ValueError('Exception: Empty List')