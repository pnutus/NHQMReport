import matplotlib

def plot_init(font_size =12,tick_size =8, tick_pad =6):
    font = {'family' : 'normal',
            'weight' : 'bold',
            'size'   : font_size}
            


    matplotlib.rcParams['text.usetex']=True
    matplotlib.rcParams['text.latex.unicode']=True
    
    matplotlib.rc('font', **font)

    matplotlib.rc('xtick', labelsize=tick_size) 
    matplotlib.rc('ytick', labelsize=tick_size)
    
    matplotlib.rcParams['xtick.major.pad'] = tick_pad
    matplotlib.rcParams['ytick.major.pad'] = tick_pad
    
    
    
    fig1 = matplotlib.pyplot.figure(1)
    fig1.set_figheight(8)
    fig1.set_figwidth(12)

    rect = fig1.patch
    rect.set_facecolor('white') # works with plt.show().  
                              # Does not work with plt.savefig("trial_fig.png")

    return fig1

def remove_top_right(ax):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

def show_only_bot(ax):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.get_yaxis().set_ticks([])
    ax.get_xaxis().tick_bottom()