def box_print(symbol, width, height):
    """
    Prints a box made of the given symbol, with specified width and height.
    The box has the symbol as borders and spaces inside.
    """
    
    # Validate that the symbol is a single character
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    
    # Validate that the width is large enough to form a box
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    
    # Validate that the height is large enough to form a box
    if height <= 2:
        raise Exception('Height must be greater than 2.')
