import matplotlib

matplotlib.use('TkAgg') # Use 'TkAgg' as the interactive backend

import matplotlib.pyplot as plt
import numpy as np # Often used for creating data

# 1. Define your data points
# X-coordinates
x_data = [1, 2, 3, 4, 5]
# Y-coordinates
y_data = [2, 3, 5, 7, 11] # Prime numbers

# 2. Use the scatter() function to draw the points
# marker='o' specifies the shape (default is circle)
# color='red' sets the color
plt.scatter(x_data, y_data, marker='o', color='red')

# 3. Add labels and a title for clarity
plt.xlabel("X-Axis (Input Values)")
plt.ylabel("Y-Axis (Output Values)")
plt.title("Simple Data Point Plot")


plt.get_current_fig_manager().set_window_title('Data Point Visualization')
# 4. Display the plot
plt.grid(True) # Optional: Adds a grid for better readability
plt.show()