class FlatIterator:

    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists

    def __iter__(self):
        self.iterator = iter(self.list_of_lists)
        self.iters = []
        return self

    def __next__(self):
        while True:
            try:
                self.element = next(self.iterator)
            except StopIteration:
                if not self.iters:
                    raise StopIteration
                else:
                    self.iterator = self.iters.pop()
                    continue
            if isinstance(self.element, list):
                self.iters.append(self.iterator)
                self.iterator = iter(self.element)
            else:
                return self.element


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]
    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()
