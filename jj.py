import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
st.title("SCRATCH LIVE DASHBOARD")
st.header("SCRATCH MONTHLY UPDATES")
df=pd.read_csv("C:/Users/uzing/Documents/Enrollment Metrics - Youth Coding 2023 - Mufakose.csv")
print(df)
df.plot.bar(x="School Name", y="Number of lessons per week")
plt.title("Lessons attended per school")
plt.ylabel("# of lessons")
plt.xlabel("Schools")
plt.show()

