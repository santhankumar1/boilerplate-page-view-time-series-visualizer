import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df =pd.csv_read("fcc-forum-pageviews.csv")

# Clean data
df =df.loc[
    (df['value']>=df['value'].quantile(0.025))&
    (df['value']>=df['value'].quantile(0.975))]


def draw_line_plot():
    fig,ax=plt.subplots(figsize=(10,5))
    ax.plot(df.index , df['value'] ,"r")
    
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("pageviews")
    # Draw line plot





    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    
    df['month']=df.index.month
    df['year']=df.index.year
    df_bar=df.groupby(['year','month'])["value"].mean()
    df_bar=df_bar.unstack()
    
    
    fig=df_bar.plot.bar(legend=True,figsize=(13,6),ylabel="Average page views",xlabel="Years").figure
    plt.legend([
        "January", "February"," March", "April", "May", "June", "July", "August", "September", "October", "November","December"
    ])
    
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=20)
    
    # Copy and modify data for monthly bar plot
    

    # Draw bar plot





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
    fig,(ax1,ax2)=plt.subplots(1,2 ,figsize=(16,8))
    sns.boxplot (data=df_box ,ax= ax1,x='year',y='value')
    ax1.set_title("Year-wise Box plot(Trend)")
    ax1.set_xlabel('Year')
    ax1.set_ylabel('value')
    
    
    sns.boxplot(data= df_box,ax= ax2,x='month',y='value')
    ax2.set_title("Month-wise Box plot(Trend)")
    ax2.set_xlabel('Month')
    ax2.set_ylabel('value')





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
