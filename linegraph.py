#importing pyplot 
from matplotlib import pyplot as plt
from matplotlib import style

x=[5,8,10]
y=[12,16,14]
x2=[6,9,11]
y2=[6,15,19]

plt.plot(x,y,'b',label='Team A',linewidth=1)
plt.plot(x2,y2,'m',label='Team B',linewidth=5)


plt.title('Team performance')
plt.ylabel('Runs')
plt.xlabel('overs')
#plt.legend()


plt.show()
