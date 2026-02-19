import pandas as pd

data = {
    'Name': ['A', 'B', 'C', 'D', 'E'],
    'Class': [10, 10, 9, 9, 10],
    'Math': [78, 45, 88, 40, 70],
    'English': [85, 55, 92, 35, 75],
    'Science': [90, 60, 95, 50, 80]
}

# Create DataFrame
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# Add Total column
df["Total"] = df[["Math", "English", "Science"]].sum(axis=1)


# Add Percentage column
df["Percentage"] = df["Total"] / 3

# Students with Percentage > 75
high = df[df["Percentage"] > 75]
print("\nStudents with Percentage > 75:\n", high)

# Sort by Percentage
s = df.sort_values("Percentage", ascending=False)
print("\nSorted by Percentage:\n", s)

# Students who failed (any subject < 40)
failed = df[
    (df["Math"] < 40) |
    (df["English"] < 40) |
    (df["Science"] < 40)
]
print("\nFailed Students:\n", failed)

print("\nFinal DataFrame:\n", df)
