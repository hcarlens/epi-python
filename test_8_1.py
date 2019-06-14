from solution_8_1 import Stack


def test_max_stack_simple():
    s = Stack()

    s.push(5)
    assert s.max() == 5

    s.push(2)
    assert s.max() == 5

    s.push(7)
    assert s.max() == 7


def test_max_stack_remove():
    s = Stack()

    s.push(5)
    s.push(2)
    s.push(7)

    assert s.pop() == 7
    assert s.max() == 5
