import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the results file
data_path = os.path.join("data", "validated_results.csv")
df = pd.read_csv(data_path)

# Create output folder for plots if it doesn't exist
os.makedirs("figures", exist_ok=True)

# Plot 1: Distribution of mod_sum values
plt.figure(figsize=(10, 6))
sns.histplot(df["mod_sum"], bins=30, kde=True, color="skyblue")
plt.title("Distribution of mod_sum values")
plt.xlabel("mod_sum")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("figures/mod_sum_distribution.png")
plt.close()

# Plot 2: Proportion of is_zero == True vs False
plt.figure(figsize=(6, 6))
df["is_zero"].value_counts().plot.pie(autopct="%1.1f%%", labels=["True", "False"], colors=["lightgreen", "salmon"])
plt.title("Conjecture Validity (is_zero)")
plt.ylabel("")
plt.tight_layout()
plt.savefig("figures/is_zero_ratio.png")
plt.close()

print("Plots saved in the 'figures/' folder.")
