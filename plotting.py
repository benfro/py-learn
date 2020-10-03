import matplotlib.pyplot as plt

data = [2, 5, 3, 7, 6, 9, 45, 23, 17, 4]

# fig, ax = plt.subplots()
# ax.plot(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], data)

# plt.plot(data)
# plt.ylabel('some numbers')
# plt.show()

def plotInternal(data, **kwargs):
    if kwargs["xlabel"]:
        plt.xlabel(kwargs["xlabel"])
    plt.plot(data)
    plt.ylabel('some numbers')
    plt.show()

plotInternal(data, xlabel="sume dumbo jumbo")



