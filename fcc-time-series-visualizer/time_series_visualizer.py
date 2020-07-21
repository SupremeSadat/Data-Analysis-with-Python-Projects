import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=['date'], index_col='date')
print(df.head())
print(df.columns)

# Clean data
df = df.loc[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]
print(df.size)

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(32, 10))
    sns.lineplot(data=df, y='value', x=df.index, color="red")
    ax.set(xlabel='Date', ylabel='Page Views', title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['date'] = df_bar.index
    df_bar["Year"] = df_bar['date'].map(lambda x: x.strftime('%Y'))
    df_bar['Month'] = df_bar['date'].map(lambda x: x.strftime('%B'))

    df_bar = pd.DataFrame(
        {'Average Page Views': df_bar.groupby(['Year', 'Month'])['value'].mean()}).reset_index().sort_values(
        ['Year', 'Month'], ascending=[1, 1])
    # Draw bar plot
    order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
             'November', 'December']
    fig, ax = plt.subplots(figsize=(30, 15))
    bar_plot = sns.barplot(x='Year', y='Average Page Views', hue='Month', hue_order=order, data=df_bar, palette='bright')
    ax.set(xlabel='Years', ylabel='Average Page Views')
    ax.legend(loc=2)





    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    fig, ax = plt.subplots(ncols=2, figsize=(32, 11))
    sns.boxplot(x='year', y="value", data=df_box, ax=ax[0])
    sns.boxplot(x='month', y="value", order=order, data=df_box, ax=ax[1])
    ax[0].set(xlabel="Year", ylabel="Page Views", title="Year-wise Box Plot (Trend)")
    ax[1].set(xlabel="Month", ylabel="Page Views", title="Month-wise Box Plot (Seasonality)")




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
