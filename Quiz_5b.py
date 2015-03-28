
# Link: http://www.codeskulptor.org/#user39_LuvFsdrUiB_20.py

# Quiz 5b, Question 1
print {}
print dict()
print

# Quiz 5b, Question 2
favorites = {'color': 'yellow', 'number': 1234567}
print favorites
favorites["fruit"] = "blackberry"
favorites["coordinate"] = (66,77)
favorite = {"fruit" : "blackberry"} # this creat a new dictionary not adding a new key.
print favorites
print favorite
print

# Quiz 5b, Question 3
# No Dictionaries, Strings, No Lists, Numbers, Booleans, Tuples
print

# Quiz 5b, Question 4
# Booleans, Strings, Dictionaries, Numbers, Lists, Tuples
print

# Quiz 5b, Question 5
for key, value in favorites.items():
    print key, value
print

# Quiz 5b, Question 7
import random

def random_point():
    """Returns a random point on a 100x100 grid."""
    return (random.randrange(100), random.randrange(100))
'''
def starting_points(players):
    """Returns a list of random points, one for each player."""
    points = []
    for player in players:
        point = random_point()
        points.append(point) #points.extend(point) #point.append(point)
    return points
'''

def starting_points(players):
    """Returns a list of random points, one for each player."""
    return [random_point() for player in players]# Or [random_point() for p in players]

players = [1, 2, 3]
print starting_points(players)
print

# Quiz 5b, Question 8
import simplegui

frame_size = [200, 200]
image_size = [600, 800] #[1521, 1818]

def draw(canvas):
    canvas.draw_image(image, image_size,
                      [image_size[0] / 2, image_size[1] / 2],
                      [frame_size[0] / 2, frame_size[1] / 2],
                      frame_size)

frame = simplegui.create_frame("test", frame_size[0], frame_size[1])
frame.set_draw_handler(draw)
image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/gutenberg.jpg")
frame.start()
print

# Quiz 5b, Question 9
import simplegui

image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/alphatest.png")

# Canvas size does not affect final letters drawn on the canvas.
WIDTH = 300
HEIGHT = 300

# Location of source
src_center = [220, 100]
src_size = [100, 100]

# canvas.draw_image(image, center_source, width_height_source, center_dest, width_height_dest)
# Draw an image that was previously loaded. center_source is a pair of coordinates giving the 
# position of the center of the image, while center_dest is a pair of screen coordinates specifying
# where the center of the image should be drawn on the canvas. width_height_source is a pair of 
# integers giving the size of the original image, while width_height_dest is a pair of integers
# giving the size of how the images should be drawn. 

def draw(canvas):
    canvas.draw_image(image, [src_center[0], src_center[1]], [src_size[0], src_size[1]], \
            [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])

# Create frame for scaled map
frame = simplegui.create_frame("Quiz5b, Q9", WIDTH, HEIGHT)

# register even handlers
frame.set_draw_handler(draw)

# Start frame
frame.start()
