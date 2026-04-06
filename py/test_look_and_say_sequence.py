from look_and_say_sequence import generate_next_num


def test_look_and_say_sequence1():
    start = "1"
    assert "11"== generate_next_num(start)

def test_look_and_say_sequence2():
    start = "11"
    assert "21"== generate_next_num(start)

def test_look_and_say_sequence3():
    start = "21"
    assert "1211"== generate_next_num(start)

