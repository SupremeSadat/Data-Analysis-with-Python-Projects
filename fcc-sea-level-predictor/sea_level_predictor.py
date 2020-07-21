import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np
def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots()
    plt.scatter(x='Year', y='CSIRO Adjusted Sea Level', data=df)

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    year2050 = pd.DataFrame(np.arange(1880,2014),index=np.arange(0,134), columns=['Year'])

    ax.axline(slope=slope, xy1=(2050, 2050*slope+intercept))

    # Create second line of best fit
    aft2000 = df.copy()
    aft2000 = aft2000.loc[aft2000['Year'] >= 2000]
    slope, intercept, r_value, p_value, std_err = linregress(x=aft2000['Year'], y=aft2000['CSIRO Adjusted Sea Level'])
    ax.axline(slope=slope, xy1=(2050, 2050 * slope + intercept))

    # Add labels and title

    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title("Rise in Sea Level")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
