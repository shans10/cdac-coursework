# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data: Cavendish's measurements
cavendish_data = [
    5.50,
    5.55,
    5.57,
    5.42,
    5.30,
    5.34,
    5.61,
    5.36,
    5.53,
    5.79,
    5.47,
    5.75,
    4.88,
    5.29,
    5.62,
    5.10,
    5.63,
    5.68,
    5.07,
    5.58,
    5.29,
    5.27,
    5.34,
    5.85,
    5.26,
    5.65,
    5.44,
    5.39,
    5.46,
]

# Convert to a Pandas DataFrame for easy handling
df = pd.DataFrame(cavendish_data, columns=["CAVEND"])

# a. Enter data in column one and name it CAVEND
print("\n=== Step a: Data in 'CAVEND' Column ===")
print(df)

# b. Construct a boxplot
plt.figure(figsize=(8, 5))
sns.boxplot(x=df["CAVEND"], color="skyblue")
plt.title("Boxplot of Cavendish Measurements")
plt.xlabel("CAVEND")
plt.grid(axis="x", linestyle="--", alpha=0.7)
plt.show()

# c. Construct a histogram with a suitable binwidth
plt.figure(figsize=(8, 5))
plt.hist(df["CAVEND"], bins=8, color="blue", alpha=0.7, edgecolor="black")
plt.title("Histogram of Cavendish Measurements")
plt.xlabel("CAVEND")
plt.ylabel("Frequency")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()

# d. Check for symmetry, skewness, modality, and outliers
print("\n=== Step d: Data Analysis from Plots ===")
boxplot_analysis = """
The boxplot indicates there may be some outliers on the lower side (values < 5.0).
The histogram appears roughly symmetric but slightly skewed to the left.
The data is unimodal, as there's one clear peak in the histogram.
"""
print(boxplot_analysis)

# e. Guesstimate mean and standard deviation from the histogram
print("\n=== Step e: Guesstimates ===")
print(
    "From the histogram, the mean appears to be around 5.45, and the standard deviation around 0.15."
)

# f. Calculate basic summary statistics
mean = df["CAVEND"].mean()
std_dev = df["CAVEND"].std()
quartiles = df["CAVEND"].quantile([0.25, 0.5, 0.75])
minimum = df["CAVEND"].min()
maximum = df["CAVEND"].max()

print("\n=== Step f: Basic Summary Statistics ===")
print(f"Mean: {mean:.2f}")
print(f"Standard Deviation: {std_dev:.2f}")
print(f"Quartiles:\n{quartiles}")
print(f"Minimum: {minimum}")
print(f"Maximum: {maximum}")

# g. Proportions within 1 and 2 standard deviations
within_1_std = df[(df["CAVEND"] >= mean - std_dev) & (df["CAVEND"] <= mean + std_dev)]
within_2_std = df[
    (df["CAVEND"] >= mean - 2 * std_dev) & (df["CAVEND"] <= mean + 2 * std_dev)
]

proportion_1_std = len(within_1_std) / len(df)
proportion_2_std = len(within_2_std) / len(df)

print("\n=== Step g: Proportions within Standard Deviations ===")
print(f"Proportion within ±1 SD: {proportion_1_std:.2%}")
print(f"Proportion within ±2 SD: {proportion_2_std:.2%}")

# Rule of thumb comparison
rule_of_thumb = """
The empirical rule states:
- About 68% of the data should fall within ±1 standard deviation.
- About 95% of the data should fall within ±2 standard deviations.
"""
print(rule_of_thumb)
