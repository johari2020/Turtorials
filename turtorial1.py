from ggame import App
myapp = App()
myapp.run()

from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# Three priamary colors with not transparency (alpha = 1.0)
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
 

# Define a line style that is a thin (1 pixel) wide black line
thinline = LineStyle(2, black)

rectangle = RectangleAsset(200, 80, thinline, blue) 

ellipse = EllipseAsset(200, 80, thinline, red) 

Sprite(rectangle, (200, 50)) 
Sprite(rectangle, (100,25))

Sprite(ellipse, (200,200))

myapp = App()
myapp.run()