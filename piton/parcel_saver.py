def save_parcel_details(length, width, height, weight):
    with open('parcel_details.txt', 'a') as file:
        file.write(f'Length: {length} cm\n')
        file.write(f'Width: {width} cm\n')
        file.write(f'Height: {height} cm\n')
        file.write(f'Weight: {weight} kg\n')
        file.write('---\n')