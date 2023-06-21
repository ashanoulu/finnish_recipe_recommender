import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
matplotlib.use('TkAgg')

# Load the dataset into a Pandas DataFrame
data = pd.read_excel('Datasets/new_data_set.xlsx')
data.fillna('', inplace=True)
# Select the two columns of interest and assign them to variables
variable1 = []
variable2 = []
for i in data.index:
    print(data['finn_sentiment_score'][i])
    print(data['num_of_words'][i])
    if data['finn_sentiment_score'][i] != 0:
        # variable1.append(data['finn_sentiment_score'][i])
        variable1.append(data['finn_sentiment_score'][i])
        variable2.append(data['Suola (Salt)'][i])

        # Calculating the coefficient
        coefficient = np.corrcoef(variable1, variable2)[0, 1]
column_1 = pd.Series(variable1) # data['Time']
column_2 = pd.Series(variable2) # data['finn_sentiment_score']

# Calculate the correlation between the two columns
correlation = column_1.corr(column_2)

print(coefficient)

# Create a scatter plot using Matplotlib
plt.scatter(column_1, column_2)
plt.xlabel('AFINN Sentiment')
plt.ylabel('Suola (Salt)')
plt.title('Correlation: {:.2f}'.format(correlation))
plt.show()

