import matplotlib.pyplot as plt
import mpltern
import pandas as pd
import matplotlib


matplotlib.use('TkAgg')

df = pd.read_excel('Datasets/new_data_set.xlsx', na_values=['N/A'])
df.fillna('N/A', inplace=True)

# Create a ternary plot
fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot(projection='ternary')
ax.set_title("Sentiment Analysis")
ax.set_xlabel("Negative")
ax.set_ylabel("Positive")
ax.set_label("Neutral")
count = 0
neucount = 0
negcount = 0
poscount = 0
# Plot the data
for i in df.index:
    print(df['finn_sentiment'][i])
    if df['finn_sentiment'][i] == 'NEUTRAL':
        neucount = neucount + 1
    if df['finn_sentiment'][i] == 'NEGATIVE':
        negcount = negcount + 1
    if df['finn_sentiment'][i] == 'POSITIVE':
        poscount = poscount + 1
    if df['finn_sentiment'][i] != 'N/A':
        count = count + 1
        ll = [(df['vader_negative'][i] + df['vader_neutral'][i] / 2)]
        ax.scatter([df['vader_negative'][i]], [df['vader_positive'][i]], [df['vader_neutral'][i]], marker='o', color='blue')
        # ax.scatter([0.8], [0.0], [0.2], marker='o', color='blue')

# for i, (x, y, z) in enumerate(data):
#     ax.scatter([(y + z / 2)], [(x + z / 2)], [(x + y + z)], marker='o', color='blue')
print(negcount, neucount, poscount)
plt.show()
