from turtle import Turtle

def tree(plist,l,a,f):

    if l>5:

        lst=[]

    for p in plist:

        p.forward(l)

        q=p.clone()

        p.left(a)

        q.right(a)

        lst.append(p)

        lst.append(q)

    tree(lst,l*f,a,f)

def main():

    p=Turtle()

    p.color('green')

    p.pensize(11)

    p.hideturtle()

    p.speed(4)

    #    p.getscreen().tracer(30,0)

    p.left(90)

    p.penup()

    p.goto(0,-100)

    p.pendown()

    t = tree([p],110,65,0.6375)

main()