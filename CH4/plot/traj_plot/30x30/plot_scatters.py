import os
import logging
logging.basicConfig(level=logging.INFO)
import argparse

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from scaks.utilities.format_utilities import convert_time

def process_interval(sites):
    new_sites = []
    for x, y, z in sites:
        if int(x) != x:
            x = (x - int(x))*(0.25/0.4) + int(x)
        new_sites.append([x, y, z])
    return new_sites

def shift(sites):
    new_sites = []
    indices = list(range(0, len(sites), 6))

    shift_indices = []
    for idx in indices:
        shift_indices.extend([idx, idx+1, idx+2])

    for i, (x, y, z) in enumerate(sites):
        if i in shift_indices:
            x += 0.5
        new_sites.append([x, y, z])
    return new_sites


def plot_scatters(types,
                  shape,
                  coordinates,
                  possible_types,
                  color_dict,
                  time, step,
                  circle_attrs=None):
    """
    Function to plot lattice grid.

    Parameters:
    -----------
    types: The site types at the lattice points as a list,
           list of strings.

    possible_types: A list of possible types, list of strings.

    color_dict: circle color for different types.
                e.g. {type: color_code}, dict.

    time: time for the configure, float.

    circle_attrs: same as **kwargs in plt.patch()
                  (http://matplotlib.org/api/patches_api.html), dict.
    """
    # Check consistency of color_dict and types.
    consistent = np.array([t in color_dict for t in possible_types]).all()
    if not consistent:
        raise ValueError('All possible type should be in color_dict.')

    # Set containers.
    fig = plt.figure(figsize=(80, 80))
    #ax = fig.add_subplot(111)
    ax = plt.gca()
    ax.set_position([-0, -0.1, 1.2, 1.2])
    ax.set_aspect('equal', adjustable='box')

    # Get scatter attrs
    alpha = circle_attrs['alpha'] if 'alpha' in circle_attrs else 0.7
    if "area" not in circle_attrs:
        area = 60.0**2/len(types)*20
    else:
        area = circle_attrs['area']

    # Classify points.
    scatter_dict = {}  # {adsorbate string: list of points}
    for t in possible_types:
        scatter_dict.setdefault(t, [])

    for t, coord in zip(types, coordinates):
        scatter_dict[t].append(coord[: 2])

    #for t, pts in scatter_dict.items():
    for t in possible_types:
        pts = scatter_dict[t]
        if not pts:
            continue
        x, y = zip(*pts)
        color = color_dict[t]
        alpha = circle_attrs['alpha'] if 'alpha' in circle_attrs else 0.7
        edgecolor = circle_attrs['edgecolor'] if 'edgecolor' in circle_attrs else color
        if t == '*_v':
            edgecolor = '#000000'
        marker = circle_attrs['marker'] if 'marker' in circle_attrs else 's'
        ax.scatter(x, y, s=area, c=color, alpha=alpha, edgecolor=edgecolor, label=t, marker=marker)

    # Set axes attrs.
    ax.set_xlim(-0.5, shape[0]*1.5)
    ax.set_ylim(-0.5, shape[-1])
    ax.set_xticks([])
    ax.set_yticks([])

    # Attrs of axis.
    for spine in ax.spines.values():
        spine.set_linestyle('dashed')
        spine.set_alpha(0.0)
        spine.set_color('#AAAAAA')

    # Get proper time format
    if time < 1e-2:
        time = '%es' % time
    else:
        time = '%dh %dmin %.2fsec' % convert_time(time)
    ax.set_title('Step = %d  ( %s )' % (step, time), fontsize=100)

    return fig

if __name__ == '__main__':

    # Set argument parser.
    parser = argparse.ArgumentParser()
    parser.add_argument("-g", "--gif",
                        help="create gif animated picture.",
                        action="store_true")
    args = parser.parse_args()

    shape = (30, 30)

    possible_types = ['*_c', '*_o', 'H_o', 'CH3_c', 'CH3_o', '-CH2_o',
                      'O2_c', 'OH_c', 'CHO_o', 'OOH_c', '*_v', 'O_c']

    color_dict = {
        '*_c': '#3913CA',
        '*_o': '#FB0101',
        'H_o': '#08DA20',
        'CH3_c': '#5E5F5E',
        'CH3_o': '#5E5F5E',
        '-CH2_o': '#FECA00',
        'O2_c': '#970000',
        'OH_c': '#D500FE',
        'CHO_o': '#009CDF',
        'OOH_c': '#79E214',
        '*_v': '#FFFFFF',
        'O_c': '#FB0101',
    }

    circle_attrs = dict(area=1500.0,
                        alpha=1.0,
                        antialiased=True,
                        marker='o'
                        )

    # Locate trajectory file.
    filename = 'auto_lattice_trajectory.py'
    if not os.path.exists(filename):
        raise IOError('No trajectory file found.')

    # Read data from file.
    globs = {}
    locs = {}
    exec(open(filename, "rb").read(), globs, locs)

    steps = locs["steps"]
    times = locs["times"]
    sites = locs["sites"]
    types = locs["types"]
    images = []
    path = "./trajplots/"

    # Get cartisian coordinates.
    cell_vectors = np.matrix([[1.0, 0.0, 0.0],
                              [0.0, 1.0, 0.0],
                              [0.0, 0.0, 1.0]])
    sites = shift(process_interval(sites))

    sites = np.matrix(sites)
    sites = (sites*cell_vectors).tolist()

    for tp, step, simu_time in zip(types, steps, times):
        if step % 2 != 0:
            continue
        fig = plot_scatters(tp, shape, sites, possible_types, color_dict,
                            time=simu_time, step=step, circle_attrs=circle_attrs)
        if not os.path.exists(path):
            os.mkdir(path)
        fname = path + str(step) + '.png'

        if os.path.exists(path):
            fname = "{}{}-redis.png".format(path, step)

        logging.info("creating {} ...".format(fname))
        fig.savefig(fname)

        # Clear figure object after saving.
        plt.close(fig)
        logging.info("Ok.")

