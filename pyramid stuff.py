import math
def pyramid_vol(length, width, height):
    volume = (length * width* height)/3
    return f"{volume:.2f}"
test_case = [
    (7,6,9),
    (6.6,3.3,7.7),
]

for length, width, height in test_case:
    volume = pyramid_vol( length, width,height)
    print(f"Length: {length}, Width: {width}, Height: {height} = Volume: {volume} cubic units")
 

       
