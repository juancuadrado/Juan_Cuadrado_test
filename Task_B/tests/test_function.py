from Task_B_Library import function

def test_comparator_versions():
    assert function.comparator_versions("1.20.1","1.20") == "version 1.20.1 is greater than version 1.20"
    