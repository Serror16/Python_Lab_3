class Stack:
    """
    Реализация стека на list.
    """

    def __init__(self):
        self._items = []

    def push(self, x: int) -> None:
        """
        Добавляет элемент x на вершину стека.
        """
        self._items.append(x)

    def pop(self) -> int:
        """
        Удаляет и возвращает элемент с вершины стека.
        Выбрасывает исключение при пустом стеке.
        """
        if self.is_empty():
            raise ValueError("Стек пуст, невозможно выполнить pop")
        return self._items.pop()

    def peek(self) -> int:
        """
        Возвращает элемент с вершины стека без его удаления.
        Выбрасывает исключение при пустом стеке.
        """
        if self.is_empty():
            raise ValueError("Стек пуст, невозможно выполнить peek")
        return self._items[-1]

    def is_empty(self) -> bool:
        """
        Проверяет, пуст ли стек.
        """
        return len(self._items) == 0

    def __len__(self) -> int:
        """
        Возвращает количество элементов в стеке.
        """
        return len(self._items)
    
    def min(self) -> int:
        """
        Возвращает минимальный элемент в стеке.
        Выбрасывает исключение при пустом стеке.
        """
        if self.is_empty():
            raise ValueError("Стек пуст, невозможно определить минимальный элемент")
        return min(self._items)