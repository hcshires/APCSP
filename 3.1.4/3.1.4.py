# Plot on one set of axes.
import matplotlib.pyplot as plt

colors = ['#4286f4', '#b2b2b2', '#ff0000', '#6a00ff', '#ff5d00', '#ff00e9', '#00b6ff', '#00ff43']
shares = [18, 17, 15, 8, 7, 7, 2, 26] # In percentages
labels = ["Samsung", "Apple", "Huawei", "Oppo", "Xiaomi", "Vivo", "Motorola", "Others"] # Each type of phone

fig, ax = plt.subplots(1,1)
ax.pie(shares, labels=labels, colors=colors, autopct='%.0f%%')

ax.set_aspect(1)
ax.set_title('Percent Global Market Share of Smartphones in Q4 of 2018')
plt.show()
