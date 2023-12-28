import src.my_functions as my_function


def test_add():
    """
    Test function to check the 'add' function with integer inputs.
    """
    result = my_function.add(number_one=1, number_two=4)
    assert result == 5
