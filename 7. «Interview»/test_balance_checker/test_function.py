import pytest
from main import check_balance


class TestBalanceChecker:
    fixtures = [
        ('()', 'Сбалансировано'),
        ('((({}]))', 'Не сбалансировано'),
        ('({[{((([])))}]}})', 'Не сбалансировано'),
        (555, None),
        ('', None),
        ('!~2piu', 'Проверяемая строка должна состоять только из скобок')
    ]

    @pytest.mark.parametrize('test_line, answer', fixtures)
    def test_check_balance(self, test_line, answer):
        result = check_balance(test_line)
        assert answer == result


if __name__ == "__main__":
    pytest.main()
