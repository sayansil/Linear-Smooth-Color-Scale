def h2rgb(h):
    s = 1
    v = 1
	
    h = (h % 360) /60
    i = int(h)
    ff = h - i

    if i == 0:
        x = v * (1 - s)
        z = v * (1 - (s * (1 - ff)))
        r, g, b = v, z, x
    elif i == 1:
        x = v * (1 - s)
        y = v * (1 - (s * ff))
        r, g, b = y, v, x
    elif i == 2:
        x = v * (1 - s)
        z = v * (1 - (s * (1 - ff)))
        r, g, b = x, v, z
    elif i == 3:
        x = v * (1 - s)
        y = v * (1 - (s * ff))
        r, g, b = x, y, v
    elif i == 4:
        x = v * (1 - s)
        z = v * (1 - (s * (1 - ff)))
        r, g, b = z, x, v
    else:
        x = v * (1 - s)
        y = v * (1 - (s * ff))
        r, g, b = v, x, y

    r = int(r*255)
    g = int(g*255)
    b = int(b*255)
    return r,g,b
