import numpy as np
from matplotlib import cm

# Create a series of color handles from colormap
def createmap(nn,cmap):
  mapvec = []
  for j in range(0,nn):
    idd = np.rint(j*256/(nn-1))
    idd = idd.astype(int)
    mapvec.append(cmap(idd))
  return mapvec

# Break down a temporal series into a smaller set of (windowed) time averages
def seqaveraging(field,n,axis=0):
  avearr = []
  m = field.shape[0]//n
  for i in range(n):
    avearr.append(np.mean(field[i*m:(i+1)*m],axis=0))
  avearr = np.stack(avearr,axis=0)
  return avearr

# Find zeroes of a function within bounds
def Cfun(x):
  return -7.0785e-3+1.8217e-7*x+4.2679e-12*x**2
p_star = optimize.brentq(Cfun, xmin, xmax) 

# Create a colormap that fits [not always...] nicely close to the plot
def colorbar(mappable):
  ax = mappable.axes
  fig = ax.figure
  divider = make_axes_locatable(ax)
  cax = divider.append_axes("right", size="5%", pad=0.05)
  return fig.colorbar(mappable, cax=cax)

# Make a function take arguments from command line using docopt
python3 test.py files/* --option1=value1 ...
"""
Usage:
    test.py <files> [options] 
Options:
    --option1=<option1>		option1 [default: value]
"""
from docopt import docopt
args = docopt(__doc__)