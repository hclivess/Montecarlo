# Montecarlo
Basic Montecarlo distribution simulator to determine volume difference between a circle of radius `r` and a rectangle of a side length `r` based on a sample of randomly placed points in a plane. Requirements include `pycairo` for graphic output. The difference with a large sample of data will yield a result close to `pi`. You can change the number of points by adjusting `balls = Balls(plane=plane, count=50)`.

## Output preview: 
- In plane: 40
- In circle: 7
- In rectangle: 3

![montecarlo](montecarlo.png)
