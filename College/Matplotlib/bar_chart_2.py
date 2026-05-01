import pandas as pd
from matplotlib import pyplot as plt
from collections import Counter

plt.style.use('fivethirtyeight')

data = pd.read_csv('bar_chart_data.csv')
ids = data['Responder_id']
languages = data['Languages']
language_counter = Counter()

for response in languages:
    language_counter.update(response.split(';'))

languages = []
popularity = []

for item in language_counter.most_common(10):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)
plt.title("Most popular Languages")
plt.xlabel("Number of People Who Use")
plt.show()
plt.savefig('bar_chart')