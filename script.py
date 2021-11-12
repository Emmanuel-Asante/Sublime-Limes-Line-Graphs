# Import modules
import codecademylib
from matplotlib import pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

visits_per_month = [9695, 7909, 10831, 12942, 12495, 16794, 14161, 12762, 12777, 12439, 10309, 8724]

# numbers of limes of different species sold each month
key_limes_per_month = [92.0, 109.0, 124.0, 70.0, 101.0, 79.0, 106.0, 101.0, 103.0, 90.0, 102.0, 106.0]
persian_limes_per_month = [67.0, 51.0, 57.0, 54.0, 83.0, 90.0, 52.0, 63.0, 51.0, 44.0, 64.0, 78.0]
blood_limes_per_month = [75.0, 75.0, 76.0, 71.0, 74.0, 77.0, 69.0, 80.0, 63.0, 69.0, 73.0, 82.0]


# create your figure here

# Create a figure of width 12 and height 8
plt.figure(figsize=(12, 8))

# Create a left subplot and save it as ax1
ax1 = plt.subplot(1,2,1)

# Create the list of x-values and store as x_values
x_values = range(len(months))

# Plot visits_per_month against x_values
plt.plot(x_values, visits_per_month, marker='o')

# Label the x-axis with descriptive titles of measure
plt.xlabel('Months')

# Label the y-axis with descriptive titles of measure
plt.ylabel('Visitors')

# Set x-axis ticks as x_values
ax1.set_xticks(x_values)

# Label x-axis tick labels as the names stored in the month list
ax1.set_xticklabels(months)

# Set title
plt.title('Page Visits Per Month')

# Customize spacing
plt.subplots_adjust(wspace=0.5)

# Create a right subplot and save it as ax2
ax2 = plt.subplot(1,2,2)

# Plot key_limes_per_month against x_values
plt.plot(x_values, key_limes_per_month, color='red')

# Plot persian_limes_per_month against x_values
plt.plot(x_values, persian_limes_per_month, color='#000000')

# Plot blood_limes_per_month against x_values
plt.plot(x_values, blood_limes_per_month, color='green')

# Add legend to lines
plt.legend(['Key Limes', 'Persian Limes', 'Blood Limes'], loc=0)

# Set x-axis ticks as x_values
ax2.set_xticks(x_values)

# Label x-axis tick labels as the names stored in the month list
ax2.set_xticklabels(months)

# Label the x-axis with descriptive titles of measure
plt.xlabel('Months')

# Label the y-axis with descriptive titles of measure
plt.ylabel('Limes Sold')

# Set titles
plt.title('Lime Sales Per Month')

# Show plots
plt.show()

# Save figure as "png" file type
plt.savefig('sublime_limes_line_graphs.png')