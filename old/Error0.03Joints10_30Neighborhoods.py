import numpy as np
import matplotlib.pyplot as plt

ls = 'dotted'
fig, ax = plt.subplots(figsize=(5,3))


x = np.array([
2,
4,
6,
8,
10,
12,
16
              ])




# 10 joints
y = np.array([
5.53,
5.39,
5.45,
5.46,
4.98,
4.37,
4.08



])

errors = np.array([
3.68,
3.71,
3.67,
3.67,
3.53,
3.29,

3.14


])

# standard error bars
ax.errorbar(x, y, yerr=errors, marker='o', markersize=8,linestyle=ls,label='10 joints',color="tab:red")
ax.errorbar(x, y+errors, marker='_', markersize=12,color='tab:red',linestyle='none')
ax.errorbar(x, y-errors, marker='_', markersize=12,color='tab:red',linestyle='none')

# 20 joints
y = np.array([
4.7,
4.79,
4.72,
4.77,
4.82,
5.05,

4.9





])

errors = np.array([
2.09,
2.03,
2.07,
2.08,
2.09,
2.16,

2.36





])

# standard error bars
ax.errorbar(x, y, yerr=errors, marker='v', markersize=8,linestyle=ls,label='20 joints',color="tab:purple")
ax.errorbar(x, y+errors, marker='_', markersize=12,color='tab:purple',linestyle='none')
ax.errorbar(x, y-errors, marker='_', markersize=12,color='tab:purple',linestyle='none')


# 30 joints
y = np.array([
3.77,
3.73,
3.75,
3.72,
3.8,
3.88,

4.05






])

errors = np.array([
1.76,
1.76,
1.76,
1.78,
1.77,
1.83,

2.02





])

# standard error bars
ax.errorbar(x, y, yerr=errors, marker='D', markersize=8,linestyle=ls,label='30 joints',color="tab:cyan")
ax.errorbar(x, y+errors, marker='_', markersize=12,color='tab:cyan',linestyle='none')
ax.errorbar(x, y-errors, marker='_', markersize=12,color='tab:cyan',linestyle='none')


"""# including upper limits
ax.errorbar(x, y + 0.5, xerr=xerr, yerr=yerr, uplims=uplims,
            linestyle=ls)

# including lower limits
ax.errorbar(x, y + 1.0, xerr=xerr, yerr=yerr, lolims=lolims,
            linestyle=ls)

# including upper and lower limits
ax.errorbar(x, y + 1.5, xerr=xerr, yerr=yerr,
            lolims=lolims, uplims=uplims,
            marker='o', markersize=8,
            linestyle=ls)

# Plot a series with lower and upper limits in both x & y
# constant x-error with varying y-error
xerr = 0.2
yerr = np.full_like(x, 0.2)
yerr[[3, 6]] = 0.3

# mock up some limits by modifying previous data
xlolims = lolims
xuplims = uplims
lolims = np.zeros_like(x)
uplims = np.zeros_like(x)
lolims[[6]] = True  # only limited at this index
uplims[[3]] = True  # only limited at this index

# do the plotting
ax.errorbar(x, y + 2.1, xerr=xerr, yerr=yerr,
            xlolims=xlolims, xuplims=xuplims,
            uplims=uplims, lolims=lolims,
            marker='o', markersize=8,
            linestyle='none')"""

# tidy up the figure
#ax.set_xlim((0, 5.5))
ax.set_ylim((0, 10.0))
#ax.set_title('0.01')
plt.grid()

#plt.xscale("log")
ax.set_xlabel('Neihborhood sizes')  # Add an x-label to the axes.
ax.set_ylabel('Distance from goal (%)')  # Add a y-label to the axes.
plt.legend()
plt.savefig("Figures/"+"Error0.03Joints10_30Neighborhoods"+".png",bbox_inches='tight')
#plt.show()

