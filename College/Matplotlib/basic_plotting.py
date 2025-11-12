from matplotlib import pyplot as plt

plt.style.use('grayscale')

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]
plt.plot(ages_x, dev_y, color="#CDF617", linestyle='--', marker='.', label='All Devs')

py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]
plt.plot(ages_x, py_dev_y, color="#B31A0F", label='Python Devs')

js_dev_y = [16446, 16791, 18942, 21780, 25704, 29000, 34372, 37810, 43515, 46823, 49293]
plt.plot(ages_x, js_dev_y, color="#241AEB", label='JavaScript')

plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Median Salary (USD) by Age')

plt.grid()
plt.legend()
plt.show() # Displays the graph