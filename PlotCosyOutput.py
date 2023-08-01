import pandas as pd
import matplotlib.pyplot as plt
import os
import shutil
import math
import numpy as np
from matplotlib import cm
from matplotlib.colors import Normalize
from scipy.interpolate import interpn

def density_scatter( x , y, ax = None, fig = None, sort = True, bins = 5, **kwargs )   :
    """
    Scatter plot colored by 2d histogram
    """
    if ax is None :
        fig , ax = plt.subplots()
    data , x_e, y_e = np.histogram2d( x, y, bins = bins, density = True )
    z = interpn( ( 0.5*(x_e[1:] + x_e[:-1]) , 0.5*(y_e[1:]+y_e[:-1]) ) , data , np.vstack([x,y]).T , method = "splinef2d", bounds_error = False)

    #To be sure to plot all data
    z[np.where(np.isnan(z))] = 0.0

    # Sort the points by density, so that the densest points are plotted last
    if sort :
        idx = z.argsort()
        x, y, z = x[idx], y[idx], z[idx]

    ax.scatter( x, y, c=z, **kwargs )

    norm = Normalize(vmin = np.min(z), vmax = np.max(z))
    cbar = fig.colorbar(cm.ScalarMappable(norm = norm), ax=ax)
    cbar.ax.set_ylabel('Multiplicity')

    return ax

def plot(plot, fig, df, x, y, title):
    #density_scatter(df[x], df[y], plot, fig)
    plot.scatter(df[x], df[y], c=df['color'], cmap=plt.get_cmap('Set1'), marker='.', s=8)
    plot.set_title(title)

def plotXYFromFile(filename):
    df = dataFrameFromCosyFile(filename)
    plt.scatter(df['x'], df['y'], c=df['color'])
    plt.colorbar()
    plt.show()


def removeOutputs(directory='output'):
    folder = directory
    for filename in os.listdir():
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


def dataFrameFromCosyFile(filename):
    print("The script will work on file: %s" % filename)

    df = pd.read_csv(filename,
                     skipfooter=6,
                     sep='\s*\s',
                     engine='python',
                     header=None,
                     names=["n", "x", "xp", "y", "yp", "time", "energy", "mass", "charge", "color"])
    df.shape
    df
    removed = df[df.eq("******").sum(axis=1) > 0].shape[0]
    if removed > 0:
        print("******* WARNING ********")
        print("The script removed %d lines from the file %s" % (removed, filename))
        
    df = df[df.ne("******").all(1)]
    df['radius'] = df.apply(lambda row: math.sqrt(math.pow(float(row['x']), 2) + math.pow(float(row['y']), 2)), axis=1)

    return df
