import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Dane przykładowe
data = np.random.randn(20, 3)
df = pd.DataFrame(data, columns=['A', 'B', 'C'])

# 1. Wbudowane wykresy Streamlit
st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)

# 2. Matplotlib
fig, ax = plt.subplots()
ax.scatter(df['A'], df['B'], c=df['C'])
ax.set_title("Wykres")
st.pyplot(fig)