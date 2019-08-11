import turtle as tt

def drawTriangle(points):
    tt.penup()
    tt.goto(points[2][0],points[2][1])
    tt.pendown()
    for i in points:
        tt.goto(i[0],i[1])

def getMid(p1,p2):
    return [(p1[0]+p2[0])/2, (p1[1]+p2[1])/2]

def sierpinski(points, step):
    drawTriangle(points)
    if step > 0:
        sierpinski([getMid(points[0],points[1]),points[1],getMid(points[1],points[2])], step - 1)#위쪽
        sierpinski([points[0],getMid(points[0],points[1]),getMid(points[0],points[2])], step - 1)#왼쪽
        sierpinski([getMid(points[0],points[2]),getMid(points[1],points[2]),points[2]], step - 1)#오른쪽

def main():
    tt.speed(1)
    myPoints = [[-100,-50],[0,100],[100,-50]]
    n=int(input("sierpinski triangle step:"))
    sierpinski(myPoints,n)
main()