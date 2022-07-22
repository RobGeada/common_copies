import numpy as np
import matplotlib.pyplot as plt
import math

plt.style.use('https://raw.githubusercontent.com/RobGeada/stylelibs/main/material_rh.mplstyle')


# plot a correlation matrix nicely
def correlation_plot(arr, labels, title):
    fig, ax = plt.subplots(figsize=(9, 9), dpi=150)
    ax.imshow(arr, cmap='RdBu', vmin=-1, vmax=1)

    # Show all ticks and label them with the respective list entries
    ax.set_xticks(np.arange(len(labels)), labels=labels)
    ax.set_yticks(np.arange(len(labels)), labels=labels)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    for i in range(len(labels)):
        for j in range(len(labels)):
            color = 'k' if np.abs(arr[i, j]) < .4 else 'w'
            ax.text(j, i, "{:.2f}".format(arr[i, j]), ha="center", va="center", color=color, fontsize=8)

    ax.set_title(title)
    ax.grid(False)
    fig.tight_layout()
    plt.show()


# automatically choose subplot dimensions
def auto_plot_count(n):
    pairs = []
    for i in range(1,n+1):
        j = math.ceil(n/i)
        remainder = (i*j) - n
        dist = np.abs(i-j)
        pairs.append((i,j,2*remainder+dist))
    return sorted(pairs, key=lambda x: (x[2]))[0][0:2]
