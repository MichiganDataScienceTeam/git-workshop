import time
from dataframe import DataFrame, Series

def benchmark_dataframe_operations():
    series_a = Series([1, 2], name="A")
    series_b = Series([3, 4], name="B")
    
    df1 = DataFrame([series_a, series_b])
    
    series2_c = Series([5, 6], name="C")
    series2_d = Series([7, 8], name="D") 
    
    df2 = DataFrame([series2_c, series2_d])

    start_time = time.time()
    df1.concatenate_vertically(df2)
    print(f"Dataframe Concatenate Vertically Time: {time.time() - start_time:.6f} seconds")
    
    # Add more benchmarks as necessary


if __name__ == "__main__":
    benchmark_dataframe_operations()
