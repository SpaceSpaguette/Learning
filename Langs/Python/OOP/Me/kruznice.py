def draw_tree(height, width):
    # Calculate the number of layers
    layers = height

    # Calculate the width of each layer
    layer_width = width

    # Draw the trunk
    trunk_height = int(height * 0.2)
    trunk_width = int(width * 0.1)

    # Draw the tree
    for i in range(layers):
        # Calculate the number of spaces for indentation
        indent = int((layer_width - (2 * i + 1)) / 2)

        # Draw the layer
        layer = ' ' * indent + '*' * (2 * i + 1) + ' ' * indent

        # Add leaves to the layer
        if i > 0:
            layer = layer.replace('*', 'o', int((2 * i + 1) * 0.7))

        print(layer)

    # Draw the trunk
    for _ in range(trunk_height):
        print(' ' * int((layer_width - trunk_width) / 2) + '|' * trunk_width)

# Get user input
height = int(input("Enter the height of the tree: "))
width = int(input("Enter the width of the tree: "))

# Draw the tree
draw_tree(height, width)
