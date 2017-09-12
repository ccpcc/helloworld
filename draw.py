from turtle import *


def draw_func(func,a,b):
    up()
    goto(a,int(func(a)))
    a=int(a)
    b=int(b)
    down()
    for x in range(a,b+1):
        goto(x,int(func(x)))


def half_ellipse1(a,b):
    a=a*a
    def f(x):
        return b*((1-((x*x)/a))**0.5)
    return f

def half_ellipse2(a,b):
    a=a*a
    def f(x):
        return -(b*(1-((x*x)/a))**0.5)
    return f

def ellipse(a,b):
    draw_func(half_ellipse1(a,b),-a,a)
    draw_func(half_ellipse2(a,b),-a,a)

if __name__ == "__main__":        
    pensize(5)
    speed(0)
    f=lambda x:(x*x)/100
    draw_func(f,-150,150)
