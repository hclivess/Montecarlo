# Montecarlo
Basic Montecarlo distribution simulator to determine volume difference between a circle of radius `r` and a rectangle of a side length `r` based on a sample of randomly placed points in a plane. Requirements include `pycairo` for graphic output. Number of points which ended up in the circle divided by the number of balls which ended up in the rectangle with a large sample of data will yield a result close to `Π`. You can change the number of points by adjusting `balls = Balls(plane=plane, count=50)`.

## Output preview: 
- In plane: 40
- In circle: 7
- In rectangle: 3

![montecarlo](montecarlo.png)
