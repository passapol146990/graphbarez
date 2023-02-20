from pyscript import Element
from js import document 
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
# แปลงข้อมูล ถ้าเป็นตัวหนังสือจะได้ str ถ้าเป็นเลขจะได้ int,float
def check_type(type):
    try:
        if isinstance(int(type[0]),int):
            return setList_int(type)
    except:
        return setList_str(type)
# แปลงข้อมูลจาก srt --> list
def setList_int(x):
    x = str(x)+' '
    sums = []
    a = ''
    for i in x: # loop text
        if(i == ' '): # เช็คว่าเจอช่องว่างไหม
            if '.' in a : # ถ้ามี . ให้ใส่ทศนิยม
                sums.append(float(a))
            else:
                sums.append(int(a))
            a = ''
        else:
            a += i
    return sums

def setList_str(x):
    x = x+' '
    sums = []
    a = ''
    for i in x:
        if i == ' ':
            sums.append(a)
            a =''  
        else:
            a += i
    return sums

# ตัดข้อมูลของแกน X,Y ให้เท่ากัน
def lenList(x,y):
    x = x
    y = y
    while True:
        if(len(x) == len(y)):
            return x, y
        else:
            if len(x) > len(y):
                x.pop()
            else:
                y.pop()

#  เรียกใช้งาน กราฟแท่ง
def ok_g2(*args, **kwargs):
    x2 = Element('x2').value
    y2 = Element('y2').value
    c2 = Element('c2').value

    name_x = Element('name_x2').value
    name_y = Element('name_y2').value
    title_graph = Element('title_graph2').value

    grid = document.querySelector('#grid').checked

    title = Element('title2') # ploygraph

    t = [check_type(x2),check_type(y2),check_type(c2)]

    x = np.arange(len(t[0]))
    width = 0.35

    fig,ax = plt.subplots()
    rects1 = ax.bar(x - width/2, t[0], width, label='Men')
    rects2 = ax.bar(x + width/2, t[1], width, label='Women') 

    ax.set_xlabel(name_x)
    ax.set_ylabel(name_y)
    ax.set_title(title_graph)
    ax.set_xticks(x,t[2])
    ax.legend()

    if grid:
        ax.grid()

    ax.bar_label(rects1,padding=3)
    ax.bar_label(rects2,padding=3)

    fig.tight_layout()

    title.write(fig)

def clear2(*args,**kwargs):
    title = Element('title2')
    title.element.innerHTML = "<div id='title1'></div>"
 