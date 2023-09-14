def add(a,b):
    result = a+b
    return result
#파이썬은 다형성이 내재되어 있다

def add_and_mul(a,b):
    return a+b, a*b
#파이썬을 여러 값을 리턴할 수 있다

#원하는 리턴값만 받을 수 있다 -> a,_ = add_and_mul(10,5)

#type - int float bool string - tuple set dictionary list
#multiple assignment language
#list -> 순서가 있는 자료들
#dictionary -> key+value fair
#python은 문자형이 없다
#c와 다른 수식연산자 (나눗셈, 덧셈 등)
