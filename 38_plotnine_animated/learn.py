import pandas as pd
import numpy as np
from plotnine import *
from plotnine.animation import PlotnineAnimation
import matplotlib.pyplot as plt

# for animation in the notebook
from matplotlib import rc
rc('animation', html='html5')

def plot(point:np.array):

    df = pd.DataFrame({
        'x': [point[0]],
        'y': [point[1]]
    })

    p = (ggplot(df)
         + geom_point(aes('x', 'y',), size=1)
         + lims(
             # All the plots have scales with the same limits
             x=(-5, +5),
             y=(-5, +5),
         )
         + theme_void()
         + theme(
             aspect_ratio=1,
             # Make room on the right for the legend
             subplots_adjust={'right': 0.85}
         )
    )
    return p

points = np.array([[1,1],[2,2]])

# It is better to use a generator instead of a list
plots = (plot(point) for point in points)
ani = PlotnineAnimation(plots, interval=100, repeat_delay=500)
ani.save('learn.mp4')
ani





