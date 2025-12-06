import pytest
from src.stack import Stack

@pytest.fixture
def empty_stack():
    """
    Фикстура для пустого стека.
    """
    return Stack()

@pytest.fixture
def populated_stack():
    """
    Фикстура для стека с элементами [1, 2, 3].
    """
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    return stack

def test_stack_initialization(empty_stack):
    """
    Проверка, что новый стек пуст.
    """
    assert empty_stack.is_empty()
    assert len(empty_stack) == 0

def test_stack_push(empty_stack):
    """
    Тестирование операции push.
    """
    empty_stack.push(10)
    assert len(empty_stack) == 1
    assert empty_stack.peek() == 10
    

def test_stack_peek(populated_stack):
    """
    Тестирование операции peek.
    """
    assert populated_stack.peek() == 3
    assert len(populated_stack) == 3
    assert populated_stack.peek() == 3

def test_stack_len(empty_stack):
    """
    Тестирование операции __len__.
    """
    assert len(empty_stack) == 0
    empty_stack.push(10)
    assert len(empty_stack) == 1
    empty_stack.push(20)
    assert len(empty_stack) == 2
    empty_stack.pop()
    assert len(empty_stack) == 1

def test_stack_is_empty(populated_stack):
    """
    Тестирование функции is_empty.
    """
    assert not populated_stack.is_empty()
    while not populated_stack.is_empty():
        populated_stack.pop()
    assert populated_stack.is_empty()

def test_stack_min_basic():
    """
    Базовый тест min() на разных элементах.
    """
    s = Stack()
    s.push(10)
    s.push(5)
    assert s.min() == 5
    s.push(15)
    assert s.min() == 5
    s.pop()
    assert s.min() == 5
    s.pop()
    assert s.min() == 10

def test_stack_min_with_duplicates():
    """
    Тестирование min() с дубликатами.
    """
    s = Stack()
    s.push(1)
    s.push(5)
    s.push(1)
    assert s.min() == 1
    s.pop()
    assert s.min() == 1


def test_pop_on_empty_stack_exception(empty_stack):
    """
    pop() должен вызвать ValueError на пустом стеке.
    """
    with pytest.raises(ValueError, match="Стек пуст, невозможно выполнить pop"):
        empty_stack.pop()

def test_peek_on_empty_stack_exception(empty_stack):
    """
    peek() должен вызвать ValueError на пустом стеке.
    """
    with pytest.raises(ValueError, match="Стек пуст, невозможно выполнить peek"):
        empty_stack.peek()

def test_min_on_empty_stack_exception(empty_stack):
    """
    min() должен вызвать ValueError на пустом стеке.
    """
    with pytest.raises(ValueError, match="Стек пуст, невозможно определить минимальный элемент"):
        empty_stack.min()