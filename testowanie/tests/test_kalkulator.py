import pytest


@pytest.fixture
def sample_numbers():
    return [1, 2, 3, 4, 5]

def add(a, b):
    return a + b

def add_list(numbers):
    return sum(numbers)


def test_add_both_positive_values():
    # Given
    a = 1
    b = 2

    #When
    result = add(a, b)

    # Then
    assert result == 3


def test_add_both_negative_values():
    # Given
    a = -1
    b = -2

    #When
    result = add(a, b)

    # Then
    assert result == -3


def test_both_zero_values():
    # Given
    a = 0
    b = 0

    #When
    result = add(a, b)

    # Then
    assert result == 0

@pytest.mark.parametrize("a,b,expected,message", [
    (1, 2, 3, "Addition of positive values"),
    (-1, -2, -3, "Addition of negative values"),
    (0, 0, 0, "Addition of zero values"),
])
def test_add_parameterized(a, b, expected, message):
    assert add(a, b) == expected, message


def test_add_list(sample_numbers):
    print(sample_numbers)
    assert add_list(sample_numbers) == 15

@pytest.mark.slow
def test_add_large_list():
    large_list = list(range(1, 1000001))

    n = len(large_list)
    expected_sum = n * (n + 1) / 2

    assert add_list(large_list) == expected_sum