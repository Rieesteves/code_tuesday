#histogram
from matplotlib import pyplot as plt
x=[2015,2016,2018,2020]
y=[12000,10000,16000,9000]

x2=[2015,2016,2017,2019,2020]
y2=[6000,7000,11000,15000,7000]

plt.bar(x,y,color="m", align= "center",label="INDIA")
plt.bar(x2,y2,color="g", align= "center",label="SRILANKA")

plt.title("popluation")
plt.ylabel("Count")
plt.xlabel("year")
plt.legend()
plt.show()
