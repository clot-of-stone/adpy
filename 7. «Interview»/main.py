from balance_checker import check_balance


def main():
    line_1 = '(((([{}]))))'
    line_2 = '[([])((([[[]]])))]{()}'
    line_3 = '{{[()]}}'
    line_4 = '}{}'
    line_5 = '{{[(])]}}'
    line_6 = '[[{())}]'
    print(check_balance(line_1))
    print(check_balance(line_2))
    print(check_balance(line_3))
    print(check_balance(line_4))
    print(check_balance(line_5))
    print(check_balance(line_6))


if __name__ == "__main__":
    main()
