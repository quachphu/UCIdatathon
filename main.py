import pandas as pd
import seaborn as sns
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


df = pd.read_csv("data1.csv")
df.shape 

# def main(): 
    
''' 
GOAL : The goal of this dataset is Uber’s Driver team is interested 
in predicting which driver signups are most likely to start driving
To help explore this question, we have provided a sample dataset of a cohort of driver signups in January 2016.
The data was pulled a few months after they signed up to include the result of whether they actually completed their first trip. 
It also includes several pieces of background information gather about the driver and their car.

Additional Information : 
Driver Economics: Each driver signup costs Uber money (background checks, processing, incentives, support staff time). 
If a significant percentage never complete a trip, it represents pure financial loss with zero return on investment.



Please help me , you should use python: 
1. Perform cleaning, exploratory analysis, and/or visualizations to use the provided data for this analysis (a few
sentences/plots describing your approach will suffice). What fraction of the driver signups took a first trip?


'''
