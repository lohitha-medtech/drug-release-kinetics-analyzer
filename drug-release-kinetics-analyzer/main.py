import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("drug_release.csv")

print (data)

plt.plot(data["Time"], data["Drug_Release"], marker='o')

plt.xlabel("time (hours)")
plt.ylabel("Drug Release (%)")
plt.title("Drug Release Kinetics")

plt.grid(True)
plt.show()