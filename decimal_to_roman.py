import unittest


def decimal_to_roman(decimal):
    if decimal <= 3:
        return 'I' * decimal
    elif decimal == 5:
        return 'V'
    else:
        return "X"

if __name__ == '__main__':
    unittest.main()