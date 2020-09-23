import numpy as np
import matplotlib.pyplot as plt



# 2 joints
x = np.array([
867,
2484,
4778,
7897,
11684,
16177,
27026
              ])
y = np.array([
2.18,
2.05,
1.91,
1.61,
1.39,
1.31,
1.24
])

errors = np.array([
3.54,
3.41,
3.37,
2.47,
1.79,
1.54,
1.41
])




ls = 'dotted'

fig, ax = plt.subplots(figsize=(5,3))

# standard error bars
ax.errorbar(x, y, yerr=errors, marker='o', markersize=8,linestyle=ls,label='2 joints')
ax.errorbar(x, y+errors, marker='_', markersize=12,color='tab:blue',linestyle='none')
ax.errorbar(x, y-errors, marker='_', markersize=12,color='tab:blue',linestyle='none')

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
ax.set_title('0.01')
plt.grid()
plt.xscale("log")
ax.set_xlabel('Learning Situations from Neighbors (#)')  # Add an x-label to the axes.
ax.set_ylabel('Distance from goal (%)')  # Add a y-label to the axes.
plt.legend()
plt.savefig("Figures/test.png",bbox_inches='tight')
plt.show()
