import re, os
import matplotlib.pyplot as plt
import numpy as np

pattern = r"k =\s+(\S+)\s+--> Best Accuracy:\s+(\S+)\s*$" 


dir = '/home/akshay/results/inception_v3_accuracy'

for i in [12]:#range(1,13):
    data1 = []
    data2 = []
    path1 = os.path.join(dir,f'{i}')
    with open(f"{path1}.txt") as f:
        for line in f:
            m = re.match(pattern, line)

            if m: 
                data1.append(tuple(map(float, m.groups())))

    path1 = os.path.join(dir,f'{i}'+'_perturbed')
    with open(f"{path1}.txt") as f:
        for line in f:
            m = re.match(pattern, line)

            if m: 
                data2.append(tuple(map(float, m.groups())))


    a=[]
    b=[]
    for z in enumerate(data1):
        a.append(data1[z[0]][0])
        b.append(data1[z[0]][1])
    # print(a)
    # print(b)


    a1=[]
    b1=[]
    for z in enumerate(data2):
        a1.append(data2[z[0]][0])
        b1.append(data2[z[0]][1])
    # print(a1)
    # print(b1)

    # plt.rc('text', usetex=True)
    # plt.rc('axes', linewidth=2)
    # plt.rc('font', weight='bold')

    # plt.rcParams['axes.linewidth'] = 2
    # plt.rcParams['xtick.labelsize'] = 40
    # plt.rcParams['ytick.labelsize'] = 50
    # plt.rcParams['axes.labelsize'] = 50
    plt.figure(figsize=(12,10))

    plt.plot(a,b,marker='d',label='Before',ms=15,linewidth=6,mec='black')
    plt.plot(a1,b1,marker='d',label='After',ms=15,linewidth=6,mec='black')

    plt.xticks([-2.2,  -1.8,  -1.4, -1.0,  -0.6,  -0.2, 0.2, 0.6, 1.0,  1.4,  1.8,  2.2],rotation=85)
    plt.yticks(np.arange(min(b), max(b)+1, 6.0))

    plt.xlabel('k',fontsize=30)
    plt.ylabel('Accuracy',fontsize=30)

    plt.tick_params(axis='both', which='major',labelsize=50)
    # plt.legend()
    # plt.rcParams["figure.figsize"] = (40,30)
    plt.tight_layout(pad=0)
    filename = f'{i}'
    plt.savefig(filename)

    # plt.show()


# from queue import Queue

    
# max_chat_size=10
# prev_chat = Queue(maxsize = max_chat_size)

# def history(prev_conv):
#     if prev_chat.full():
#         prev_chat.get()
#     prev_chat.put(prev_conv)




# num_items = prev_chat.qsize()
# for i in range(num_items):
#     item = prev_chat.get()
#     #codel

#     prev_chat.put(item)


    


