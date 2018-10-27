import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button


fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)
x = range(-50,50)
y = range(-50,50)

l, = plt.plot(x, y, lw=2)
ax.title.set_text('y = x')

class Index(object):
    ind = 0
    global funcs # used so yu can access local list, funcs, here
    def next(self, event):
        self.ind += 1
        i = self.ind %(len(funcs))
        x,y,name = funcs[i]() # unpack tuple data
        l.set_xdata(x) #set x value data
        l.set_ydata(y) #set y value data
        ax.title.set_text(name) # set title of graph
        plt.draw()

    def prev(self, event):
        self.ind -= 1
        i  = self.ind %(len(funcs))
        x,y, name = funcs[i]() #unpack tuple data
        l.set_xdata(x) #set x value data
        l.set_ydata(y) #set y value data
        ax.title.set_text(name) #set title of graph
        plt.draw()

def plot1():
    x = range(-20,20)
    y = x
    name = "y = x"
    return (x,y, name)

def plot2():
    x = range(-20,20)
    y = np.power(x, 2)
    name = "y = x^2"
    return (x,y,name)

def plot3():
    x = range(-20,20) # sample data
    y = np.power(x, 3)
    name = "y = x^3"
    return (x,y, name)


funcs = [plot1, plot2, plot3] # functions in a list so you can interate over
callback = Index()
axprev = plt.axes([0.7, 0.05, 0.1, 0.075])
axnext = plt.axes([0.81, 0.05, 0.1, 0.075])
bnext = Button(axnext, 'Next')
bnext.on_clicked(callback.next)
bprev = Button(axprev, 'Previous')
bprev.on_clicked(callback.prev)

plt.show()
