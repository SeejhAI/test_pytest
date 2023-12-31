import src.my_functions as my_function


def test_add():
    """
    Test function to check the 'add' function with integer inputs.
    """
    result = my_function.add(number_one=1, number_two=4)
    assert result == 5


def test_divide_two():
    """
    Test function to check the 'divide' function with normal division.
    """
    result = my_function.divide(number_one=20, number_two=5)
    assert result == 4
