
# ============================================================
# Defining your own functions here
# ============================================================

def add(a, b):
    return a + b



# ============================================================
# Defining your own testing here
# ============================================================

def test_right():
    assert add(-2, -3) == -5
    assert add('boston', 'university') == 'bostonuniversity'


def test_error():
    assert add(2, 3) == -1
