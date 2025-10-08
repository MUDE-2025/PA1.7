import debug_example as de

def test_compute_ratio_basic():
    assert de.compute_ratio(10, 2) == 5
    assert de.compute_ratio(9, 3) == 3
    assert de.compute_ratio(10, 0) == 0 # Updated to avoid ZeroDivisionError