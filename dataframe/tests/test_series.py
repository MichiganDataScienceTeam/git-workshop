from dataframe import Series
import pytest

def test_series_sum():
    series1 = Series(data=[1, 2], name="A")
    assert series1.sum() == 3


# TODO: ALL - Implement tests for all other Series methods
# Use the test_series_sum test as a reference
# Reference pytest documentation as necessary: https://docs.pytest.org/en/stable/contents.html