import matplotlib.pyplot as plt

results = open('results.txt','r')

aa, bb= [], []

for ii in results.readlines():
    aa.append(ii)

for ii in aa:
    bb.extend(ii.split())

x, f1, f2 = [], [], []
f = [x, f1, f2]
i = 0

for ii in bb:
    try:
        f[i%3].append(float(ii))
        i += 1
    except:
        f[i%3].append(1)    # sinc(0) is not defined. but limit is 1.
        i += 1

title = [0,'Gaussian', 'Sinc']
linestyle = [0, '--', ':']
color = [0, 'blue', 'red']

for i in [1,2]:
    plt.subplot(1,2,i)
    plt.plot(x,f[i],linestyle[i],color=color[i])
    plt.title(title[i])
    plt.ylabel('Y value')
    plt.xlabel('X value')
    plt.tight_layout()

plt.savefig('results.png')
