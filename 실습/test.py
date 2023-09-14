import turtle

#다중대입
a=100
b=10
print(a,b)
a,b = b,a
print(a,b)

x,y,z = 1,2,3
x,y,z = y,z,x
print(x,y,z)


#for
sum=0
for i in range(1,100+1,2): #step
    sum += i
print(sum)


for x,y,r in [(200,200,50), (-200,-200,30), (100,100,50)]:
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.circle(r)
    turtle.write(str((x,y)))
