from typing import Literal, get_args, get_origin
import inspect
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline


def plot(self, plot_type: str = 'bar', **plot_kwargs) -> None:
    '''
    Plot the normalized token attributes to have a comparative view.
    Available plot types include bar chart, horizontal bar chart, and pie chart.
    '''

    # Convert list of tuples to a dataframe
    df = pd.DataFrame(self, columns=['Tokens', 'percent']).set_index('Tokens')

    # Bar chart
    if type == 'bar':
        df.plot.bar(ylabel = 'percent',
            title = title,
            legend = False,
            rot = rot);
    
    # Horizontal bar chart
    elif type == 'barh':
        df.plot.barh(ylabel = 'percent',
            title = title,
            legend = False,
            rot = 0);

    # Pie chart
    elif type == 'pie':
        df.plot.pie(y = 'percent',
            title = title,
            legend = False,
            autopct = '%1.1f%%',
            figsize = (8, 8));

        

