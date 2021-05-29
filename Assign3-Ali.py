from matplotlib.pyplot import *
from numpy import *

t = arange(0,1,0.001)
y = 2*sin(2*pi*t)

import copy
y_sat = copt.copy(y)

figure(3)
clf()
plot(t,y, 'r--')

y_sat[y_sat > 0.5] = 0.5
y_sat[y_sat < -0.5] = -0.5

plot(t,y_sat)
ylabel('$y(t)$')
xlabel('Time(sec.)')
legend(loc=1)
show()


figure(4)
clf()
plot(t,y, 'r--')

inds1 = where(y > 0.5)[0]
y_sat[inds1] = 0.5
inds2 = where(y < -0.5)[0]
y_sat[inds2] = -0.5

plot(t,y_sat,linewidth=2.0, label ='$y(t)$')
ylabel('$y(t)$')
xlabel('Time(sec.)')
legend(loc=1)
show()


N = len(y)
y_sat = zeros(N)

for i, y_i in enumerate(y):
    if y_i > 0.5:
        y_sat[i] = 0.5
        elif y_i < -0.5:
            y_sat[i] = -0.5
            else:
                y_sat[i] = y_i
 figure(2)
 clf()
 plot(t,y,'r--')
 plot(t,y_sat, label = '$y(t)$', linewidth=2.0)
 ylabel('$y(t)$')
 xlabel('Time(sec.)')
 legend(loc=1)
 show()

 
N=len(y)
y_sat = zeros(N)

for i in range(N):
    y_i = y[i]
    if y_i > 0.5:
        y_sat[i] = 0.5
        elif y_i < -0.5:
            y_sat[i] = -0.5
            else:
                y_sat[i] = y_i
figure(1)
clf()
plot(t,y,'r--')
plot(t, y_sat, label = '$y(t)$', linewidth=2.0)
 ylabel('$y(t)$')
 xlabel('Time(sec.)')
 legend(loc=1)
 show()
        
 

        
 


