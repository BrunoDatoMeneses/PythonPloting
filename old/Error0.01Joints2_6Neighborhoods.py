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



# 6 joints
y = np.array([
4.3,
4.26,
4.32,
4.41,
4.29,
4.06,

4.5


])

errors = np.array([
5.12,
5.09,
5.08,
5.19,
5.06,
4.99,

5.29


])

# standard error bars
ax.errorbar(x, y, yerr=errors, marker='o', markersize=8,linestyle=ls,label='6 joints')
ax.errorbar(x, y+errors, marker='_', markersize=12,color='tab:blue',linestyle='none')
ax.errorbar(x, y-errors, marker='_', markersize=12,color='tab:blue',linestyle='none')

# 3 joints
y = np.array([
2.64,
2.41,
2.3,
2.55,
2.25,
2.15,
1.68

])

errors = np.array([
4.34,
3.54,
3.37,
4.06,
3.73,
3.55,
2.39

])

# standard error bars
ax.errorbar(x, y, yerr=errors, marker='v', markersize=8,linestyle=ls,label='3 joints')
ax.errorbar(x, y+errors, marker='_', markersize=12,color='tab:orange',linestyle='none')
ax.errorbar(x, y-errors, marker='_', markersize=12,color='tab:orange',linestyle='none')

# 2 joints
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

# standard error bars
ax.errorbar(x, y, yerr=errors, marker='D', markersize=8,linestyle=ls,label='2 joints')
ax.errorbar(x, y+errors, marker='_', markersize=12,color='tab:green',linestyle='none')
ax.errorbar(x, y-errors, marker='_', markersize=12,color='tab:green',linestyle='none')



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
plt.savefig("Figures/"+"Error0.01Joints2_6Neighborhoods"+".png",bbox_inches='tight')
#plt.show()

