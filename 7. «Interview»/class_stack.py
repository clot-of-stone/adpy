class Stack:
    def __init__(self) -> None:
        self.items = []

    def is_empty(self) -> bool:
        state = False
        if len(self.items) == 0:
            state = True
        return state

    def push(self, new_item) -> None:
        self.items.append(new_item)

    def pop(self) -> str:
        self.items.pop()
        if not self.is_empty():
            return self.peek()

    def peek(self) -> str:
        return self.items[-1]

    def size(self) -> int:
        return len(self.items)

    def show(self) -> list:
        return self.items

    def clear(self) -> None:
        return self.items.clear()
