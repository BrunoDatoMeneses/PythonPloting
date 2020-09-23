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
5.71,
5.42,
5.51,
5.52,
5.29,
5.6,

5.52



])

errors = np.array([
4.03,
3.94,
4.01,
4.04,
3.93,
4.01,

3.96



])

# standard error bars
ax.errorbar(x, y, yerr=errors, marker='o', markersize=8,linestyle=ls,label='10 joints',color="tab:red")
ax.errorbar(x, y+errors, marker='_', markersize=12,color='tab:red',linestyle='none')
ax.errorbar(x, y-errors, marker='_', markersize=12,color='tab:red',linestyle='none')

# 20 joints
y = np.array([
4.65,
4.55,
4.63,
4.58,
4.61,
4.63,

4.59




])

errors = np.array([
1.95,
1.93,
1.85,
1.91,
1.89,
1.96,

1.91




])

# standard error bars
ax.errorbar(x, y, yerr=errors, marker='v', markersize=8,linestyle=ls,label='20 joints',color="tab:purple")
ax.errorbar(x, y+errors, marker='_', markersize=12,color='tab:purple',linestyle='none')
ax.errorbar(x, y-errors, marker='_', markersize=12,color='tab:purple',linestyle='none')


# 30 joints
y = np.array([
3.54,
3.49,
3.43,
3.49,
3.46,
3.48,

3.5





])

errors = np.array([
1.51,
1.56,
1.51,
1.55,
1.48,
1.53,

1.55




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
plt.savefig("Figures/"+"Error0.01Joints10_30Neighborhoods"+".png",bbox_inches='tight')
#plt.show()

