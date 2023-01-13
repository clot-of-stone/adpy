from class_stack import Stack


def check_balance(line: str):
    stack = Stack()
    brackets = {'{': '}', '[': ']', '(': ')'}
    acceptable_symbols = '({[]})'
    while line and isinstance(line, str):
        for position in range(len(line)):
            if line[position] not in acceptable_symbols:
                return 'Проверяемая строка должна состоять только из скобок'
        if line[0] in brackets.values() or len(line) % 2 != 0:
            return 'Не сбалансировано'
        for item in line:
            if item in brackets.keys():
                stack.push(item)
            else:
                if stack.size() == 0:
                    return 'Не сбалансировано'
                bracket = stack.peek()
                if brackets[bracket] != item:
                    return 'Не сбалансировано'
                stack.pop()
        if stack.is_empty():
            return 'Сбалансировано'
        else:
            return 'Не сбалансировано'
