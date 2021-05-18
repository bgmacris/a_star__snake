def draw_map():
    display = 190
    chunk = 10

    positions_x = []
    positions_y = []
    while display >= 0:
        positions_x.append(display)
        positions_y.append(display)
        display -= chunk

    conexiones = {}
    for x in positions_x:
        for y in positions_y:
            tupla = (x, y)
            if tupla[0] + 10 < 200:
                if tupla in conexiones:
                    conexiones[tupla][(tupla[0] + chunk, tupla[1])] = chunk
                else:
                    conexiones[tupla] = {}
                    conexiones[tupla][(tupla[0] + chunk, tupla[1])] = chunk
            if tupla[0] - 10 > 0:
                if tupla in conexiones:
                    conexiones[tupla][(tupla[0] - chunk, tupla[1])] = chunk
                else:
                    conexiones[tupla] = {}
                    conexiones[tupla][(tupla[0] - chunk, tupla[1])] = chunk

            if tupla[1] + 10 < 200:
                if tupla in conexiones:
                    conexiones[tupla][(tupla[0], tupla[1] + chunk)] = chunk
                else:
                    conexiones[tupla] = {}
                    conexiones[tupla][(tupla[0], tupla[1] + chunk)] = chunk
            if tupla[1] - 10 > 0:
                if tupla in conexiones:
                    conexiones[tupla][(tupla[0], tupla[1] - chunk)] = chunk
                else:
                    conexiones[tupla] = {}
                    conexiones[tupla][(tupla[0], tupla[1] - chunk)] = chunk

    return conexiones


# x = draw_map()
# for i in x:
#     print(i, x[i])