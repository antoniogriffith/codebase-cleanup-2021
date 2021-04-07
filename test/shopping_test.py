# import some code we want to test
from app.shopping import format_usd

# TODO: test the code

def test_format_usd():
    assert format_usd(9.5) == "$9.50"

    #edge cases 
    assert format_usd(100000000) == "$100,000,000.00"
    assert format_usd(0.25) == "$0.25"