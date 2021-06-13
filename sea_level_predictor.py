import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    years, sea_level = linear_best_fit(df)
    plt.plot(years, sea_level, color="red")

    # Create second line of best fit
    df_2000 = df.copy()
    df_2000 = df_2000[df_2000["Year"] >= 2000]
    years_2, sea_level_2 = linear_best_fit(df_2000)
    plt.plot(years_2, sea_level_2, color="green")

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend([f"{df['Year'].min()}-2050", "2000-2050"])
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

def linear_best_fit(df):
  slope, intercept, *_ = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
  years = range(int(df["Year"].min()), 2051, 1)
  sea_level = [slope*x + intercept for x in years]

  return (years, sea_level)