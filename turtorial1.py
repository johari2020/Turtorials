from ggame import App
myapp = App()
myapp.run()

from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# Three priamary colors with not transparency (alpha = 1.0)
red = Color(0xff0000, 0.5)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
 

# Define a line style that is a thin (1 pixel) wide black line
thinline = LineStyle(2, black)

rectangle = RectangleAsset(200, 80, thinline, blue) 

ellipse = EllipseAsset(10, 10, thinline, blue) 

poly = PolygonAsset([(0,0), (100,100), (100,200), (0,0)], thinline, red)

Sprite(rectangle, (200, 50)) 

Sprite(ellipse, (250,250))

Sprite(poly, (200,200))

myapp = App()
myapp.run()