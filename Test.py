def func(x):
    return x+1

def test_answer():
    assert func(1) == 2
    assert func(2) == 3

def faire_le_café(au_régime, sucre):
    if au_régime:
        assert not sucre


faire_le_café(1,1)