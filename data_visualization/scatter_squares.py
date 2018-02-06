import matplotlib.pyplot as plt


x_values = list(range(1, 10))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, edgecolors='none', cmap=plt.cm.Blues, c=y_values, s=40)

plt.title("Scatter Numbers", fontsize=25)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=10)

plt.axis([0, 10, 0, 100])

plt.savefig('square_plot.png', bbox_inches='tight')
