import matplotlib.pyplot as plt
import numpy as np
years = [2008, 2009, 2010, 2011, 2012]
sachin = [1063,972, 1562, 756, 1357]
sehwag =[1462, 1090, 1732, 1175, 833]
kohli = [159, 325, 995, 1644, 2186]
x = np.arange(len(years))
width = 0.25
plt.bar(x - width, sachin, width=width, label = "Sachin", color = "#7DE4FF")
plt.bar(x , sehwag, width=width, label = "Sehwag", color = "#FFA27D")
plt.bar(x + width, kohli, width=width, label = "Kohli", color = "#D391FF")
plt.xticks(x , years)
plt.xlabel("Years")
plt.ylabel("Runs Scored")
plt.title("Indian Batsmen Comparison (2008–2012)")
plt.legend()
plt.show()
