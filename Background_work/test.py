import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel("Datasets/new_data_set.xlsx")
df.fillna('', inplace=True)
x = df['finn_sentiment_score'].dropna()

# Generate corresponding y-values based on indices
y = list(range(len(x)))

# Plotting the line graph
plt.plot(x, y)

# Adding labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Graph')

# Display the graph
plt.show()
