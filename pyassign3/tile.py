"""tiles.py : 计算使用a*b的砖块铺m*n的墙的方法种类数目
   并对指定的方法使用turtle进行可视化
   author: Weijie Zhou   
"""
import turtle

def pave(m, a, b, x, y, wall, s, ans):
    """在m*n的墙上铺一块
    a*b的砖块（从坐标（x，y）开始）
    并对砖块所覆盖的方块进行标记，记号为'1'
    """
    for i in range(y, y + b):
        for j in range(x, x + a):
            wall[i * m + j] = "1"
            s.append(i * m + j)
    ans.append(tuple(s))


def conflict(m, n, a, b, x, y, wall):
    """定义冲突函数，
    若不冲突则可横向铺一块砖
    铺过的标记为1，未铺过标记为0    
    """
    if y + b <= n and x + a <= m:
        for i in range(y, y + b):
            for j in range(x, x + a):
                if wall[i * m + j] == "1":
                    return True
        return False
    else:
        return True




def tile(m, n, a, b, wall, alls=[], ans=[], x=0, y=0):
    """m为墙长，n为墙宽
    a为砖长，b为砖宽
    ans中储存每一种铺法的砖块坐标
    alls中储存所有铺法的砖块坐标
    """
    s = []
    if a == b:
        if not conflict(m, n, a, b, x, y, wall):
            pave(m, a, b, x, y, wall, s, ans)
            if "0" in wall:
                p = wall.index("0")
                tile(m, n, a, b, wall, alls, ans, y=p // m, x=p % m)  
            else:
                alls.append(ans)
    else:
        if not conflict(m, n, a, b, x, y, wall) and not conflict(m, n, b, a, x, y, wall):
            ans_new = ans[:]  
            s_new = s[:]
            wall_new = wall[:]
            pave(m, a, b, x, y, wall, s, ans)
            if "0" in wall:
                r = wall.index("0")
                tile(m, n, a, b, wall, alls, ans, y=r // m, x=r % m)
            else:
                alls.append(ans)
            pave(m, b, a, x, y, wall_new, s_new, ans_new)
            if "0" in wall_new:
                g = wall_new.index("0")
                tile(m, n, a, b, wall_new, alls, ans_new, y=g // m, x=g % m)
            else:
                alls.append(ans_new)
        elif not conflict(m, n, a, b, x, y, wall):
            pave(m, a, b, x, y, wall, s, ans)
            if "0" in wall:
                r = wall.index("0")
                tile(m, n, a, b, wall, alls, ans, y=r // m, x=r % m)
            else:
                alls.append(ans)
        elif not conflict(m, n, b, a, x, y, wall):
            pave(m, b, a, x, y, wall, s, ans)
            if "0" in wall:
                r = wall.index("0")
                tile(m, n, a, b, wall, alls, ans, y=r // m, x=r % m)
            else:
                alls.append(ans)
    return alls


def draw(m, n, method):
    """使用wugui turtle来进行铺砖方式的可视化

    """
  
    wugui_1 = turtle.Turtle()
    wugui_2 = turtle.Turtle()
    wugui_1.hideturtle()
    wugui_2.hideturtle()
    wugui_1.speed(0)
    wugui_2.speed(0)
    wugui_1.pensize(10)
    wugui_2.pensize(1)
    wugui_2.color('blue')
    
    t = 250 / (m*n)**0.5
    for i in range(0,n+1):
        wugui_2.up()
        wugui_2.goto(-t * m,2*t*i - t*n)
        wugui_2.down()
        wugui_2.fd(2*t*m)
    wugui_2.lt(90)
    for j in range(0,m+1):
        wugui_2.up()
        wugui_2.goto(2*t*j - t*m,-t*n)
        wugui_2.down()
        wugui_2.fd(2*t*n)



    for i in method:
        r = max(i)
        g = min(i)
        wugui_1.up()
        x_min = 2 * (g % m) * t - m * t
        y_min = 2 * (g // m) * t - n * t
        x_max = (2 + 2 * (r % m)) * t - m * t
        y_max = (2 + 2 * (r // m)) * t - n * t
        wugui_1.goto(x_min, y_min)
        wugui_1.down()
        wugui_1.goto(x_max, y_min)
        wugui_1.goto(x_max, y_max)
        wugui_1.goto(x_min, y_max)
        wugui_1.goto(x_min, y_min)
def main():
    m = int(input("请输入墙的长度："))
    n = int(input("请输入墙的宽度："))
    a = int(input("请输入砖的长度："))
    b = int(input("请输入砖的宽度："))
    wall = ["0"] * (m*n)
    alls = tile(m, n, a, b, wall)
    num = len(alls)
    for i in alls:
        print(i)
    print("共有" + str(num) + "种方案")
    if num > 0:
        e = int(input("请选择第X种方案（第一种方法的编号为1，依此类推）："))
        draw(m, n, alls[e-1])


if __name__ == "__main__":
    main()
