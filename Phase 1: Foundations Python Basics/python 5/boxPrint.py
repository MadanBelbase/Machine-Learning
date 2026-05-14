def box_print(symbol, width, height):
    # Validate that the symbol is a single character
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    
    # Validate minimum width and height
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    if height <= 2:
        raise Exception('Height must be greater than 2.')

    # Print top border
    print(symbol * width)
    
    # Print middle section
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    
    # Print bottom border
    print(symbol * width)


# Try calling the function and handle exceptions
try:
    box_print('*', 4, 4)
    box_print('O', 20, 5)
    box_print('x', 1, 3)     # Will raise "Width must be greater than 2."
    box_print('ZZ', 3, 3)    # Will raise "Symbol must be a single character string."
except Exception as err:
    print('An exception happened: ' + str(err))

