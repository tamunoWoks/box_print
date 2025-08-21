def box_print(symbol, width, height):
    """
    Prints a box made of the given symbol, with specified width and height.
    The box has the symbol as borders and spaces inside.
    """
    
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    if height <= 2:
        raise Exception('Height must be greater than 2.')

    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)

    print(symbol * width)

# Error handling
try:
    box_print('*', 4, 4)     # Valid: 4x4 box with '*'
    box_print('O', 20, 5)    # Valid: 20x5 box with 'O'
    box_print('x', 1, 3)     # Invalid: width too small
    box_print('ZZ', 3, 3)    # Invalid: symbol is more than 1 character
except Exception as err:
    print('An exception happened: ' + str(err))

try:
    box_print('ZZ', 3, 3)    # Invalid: symbol not a single character
except Exception as err:
    print('An exception happened: ' + str(err))
