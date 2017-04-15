import matplotlib.pyplot as plt

def set_ch():
    from pylab import mpl
    mpl.rcParams['font.sans-serif'] = ['FangSong'] 
    mpl.rcParams['axes.unicode_minus'] = False 

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., 1.03*height, "%s" % float(height))

set_ch()

plt.xlabel(u"性別")
plt.ylabel(u"人數")

plt.title(u"性別比例分析")
plt.xticks((0,1),(u"男",u"女"))
rect = plt.bar(left = (0,1,2,3,4,5,6,),height = (1,0.5,0.5,0.5,0.5,0.5,0.5),width = 0.35,align="center")

plt.legend((rect,),(u"圖例",))
autolabel(rect)

plt.show()