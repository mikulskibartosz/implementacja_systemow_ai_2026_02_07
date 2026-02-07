from hypothesis import given, strategies as st

def reverse_list(lst):
    return lst[::-1]

@given(st.lists(st.integers()))
def test_reverse_twice_is_identity(lst):
    assert reverse_list(reverse_list(lst)) == lst

@given(st.integers())
def test_adding_zero_is_identity(a):
    assert a + 0 == a

@given(st.integers(), st.integers())
def test_add_commutative(a, b):
    assert a + b == b + a

@given(st.integers(), st.integers(), st.integers())
def test_add_associative(a, b, c):
    assert (a + b) + c == a + (b + c)