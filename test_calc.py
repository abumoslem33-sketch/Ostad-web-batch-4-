from calc import add


def test_add_positive_numbers():
    assert add(5,6)==11


    
def test_add_positive_add_negative_numbers():
    assert add (5,-2)==3
    