"""Example usage of the dataFrame package."""
from dataframe import DataFrame, Series

# Create Series objects for each column
series_a = Series([1, 3], name="A")
series_b = Series([2, 4], name="B")

# Create a DataFrame using the Series objects
df1 = DataFrame([series_a, series_b])

# Print the DataFrame
print(df1)


series_c = Series([1, None], name="C")
series_d = Series([None, 4], name="D")

# Create a DataFrame with NaN values
df2 = DataFrame([series_c, series_d])

# Print the DataFrame with NaN values
print(df2)
