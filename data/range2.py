import matplotlib.pyplot as plt

Medals = (8,3)
gender = ['Men', 'Woman']
colors = ['r', 'g']

plt.pie(Medals, labels=gender, colors=colors, startangle=90, autopct='%.1f%%')
plt.show()
