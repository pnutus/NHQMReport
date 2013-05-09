import matplotlib
import scipy as sp

"""
TODO


KNOWLEDGE BASE:

*empty markers:
    plot( ... , markersize=7,
    markeredgewidth=1, markeredgecolor='k',
    markerfacecolor='None')

*arrows:
    # P.arrow( x, y, dx, dy, **kwargs 
    f/ec - face/edge color)
        plt.arrow( 0.8, 0.5, 0.05, 0, fc="k", ec="w",linewidth=1,
        head_width=0.03, head_length=0.02 )

"""   

def plot_init(font_size =14,tick_size =11, tick_pad =6):
    font = {'family' : 'normal',
            'weight' : 'bold',
            'size'   : font_size}

    matplotlib.rcParams['text.usetex']=True
    matplotlib.rc('font', family='serif')
    matplotlib.rc('text', usetex=True )
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

   
def save(figure, name ="output"):
    filename = name + '.pdf' 
    try: 
        figure.savefig(filename, transparent=True, bbox_inches='tight', pad_inches=0.1)
    except:
        print "no applicable figure, asking matplotlib for a favor"
        matplotlib.pyplot.savefig(filename, transparent=True, bbox_inches='tight', pad_inches=0.1)    

def center_axis(ax):
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_smart_bounds(True)
    ax.spines['bottom'].set_smart_bounds(True)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    
def plot_contour(contour, ax=None):
    points, _ = contour
    try: ax.plot(sp.real(points), sp.imag(points), 'k*-')   
    except: matplotlib.pyplot.plot(sp.real(points), sp.imag(points), 'k*-')    