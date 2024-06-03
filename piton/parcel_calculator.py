def calculate_price(length, width, height, weight):
    # Calculate volume
    volume = length * width * height

    # Determine price based on weight and volume
    if weight <= 1:
        if volume <= 5000:
            price = 3
        elif volume <= 10000:
            price = 5
        else:
            price = 7
    elif weight <= 5:
        if volume <= 5000:
            price = 5
        elif volume <= 10000:
            price = 7
        else:
            price = 9
    else:
        if volume <= 5000:
            price = 7
        elif volume <= 10000:
            price = 9
        else:
            price = 11

    return price