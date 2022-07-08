import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def cross_plot(data, barra, variable, categorias, size=(10,7), xlim=(-0.5,3.5), ylim=(0.1,0.8), titulo = None, order=1, medias=0):
    fig, ax1 = plt.subplots(figsize=size)
    ax2 = ax1.twinx()
    if order==1:
        data = data.sort_values(barra).reset_index(drop=True)
    data[barra].plot(kind='bar', color='b', ax=ax1, label=barra)
    try:
        for v in variable:
            data[v].plot(kind='line', marker='d', ax=ax2, label=v)
    except:
        data[variable].plot(kind='line',color='r', marker='d', ax=ax2, label=variable)
    ax1.yaxis.tick_left()
    ax2.yaxis.tick_right()
    ticks = data[categorias]
    plt.xticks(np.arange(ticks.unique().shape[0]),ticks)
    plt.xlim(xlim)
    plt.ylim(ylim)
    if medias==1:
        cc = ['blue','red','gray']
        j=0
        try:
            for v in variable:
                plt.axhline(data[v].mean(), label=v, color=cc[j])
                j=j+1
        except:
            plt.axhline(data[variable].mean(), label=variable, color=cc[j])
    plt.title(titulo)# , fontdict=font)
    ax1.set_xlabel(categorias)#, fontdict=font1)
    ax1.set_ylabel(barra)#, fontdict=font1)
    ax2.set_ylabel(variable)#, fontdict=font1)
    plt.legend()
    plt.grid()
    fig.tight_layout()  
    plt.show()


def plot_hist(df, variable, bins=100):
    tmp_mean = np.mean(df[variable])
    tmp_median = np.median(df[variable])
    plt.hist(df[variable], color='dodgerblue', alpha=.7, bins=bins)
    plt.axvline(tmp_mean, color='tomato', label="Media:{0}".format(round(tmp_mean, 1)))
    plt.axvline(tmp_median, color='#f2b41e', label="Mediana: {0}".format(round(tmp_median, 1)))
    plt.title("Histograma para {0}".format(variable))
    plt.legend()
    plt.show()