def calculator(exp):
    operators = '+-*/'
    if not any(operator in exp for operator in operators):
        raise ValueError(f'expression must have one operator {operators}')
    for operator in operators:
        if operator in exp:
            try:
                left, right = exp.split(operator)
                left, right = int(left), int(right)
                if operator == '+':
                    return left + right
                elif operator == '-':
                    return left - right
                elif operator == '*':
                    return left * right
                elif operator == '/':
                    return left / right
            except (ValueError, TypeError):
                raise ValueError(
                    'expression must have two integers and one operator')


if __name__ == '__main__':
    print(calculator('10 - 10'))
