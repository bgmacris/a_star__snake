from route import algoritmo, ruta

def draw_map():
    display = 40
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
            if tupla[0] + 10 < 40:
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

            if tupla[1] + 10 < 40:
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

mapa = draw_map()

snake = []
inicio = (40, 10)
solucion = (10, 10)

ruta_corta = algoritmo(mapa, snake, inicio, solucion)
def alargar_ruta(mapa, snake, ruta_corta):
    visitados = ruta_corta

def longest_path_to(ruta_corta, cabeza):
    cur = head = cabeza
    # Set all positions on the shortest path to 'visited'
    visitados = ruta_corta
    # Extend the path between each pair of the positions
    idx, cur = 0, head
    while True:
        cur_direc = path[idx]
        nxt = cur.adj(cur_direc)
        if cur_direc == Direc.LEFT or cur_direc == Direc.RIGHT:
            tests = [Direc.UP, Direc.DOWN]
        elif cur_direc == Direc.UP or cur_direc == Direc.DOWN:
            tests = [Direc.LEFT, Direc.RIGHT]
        extended = False
        for test_direc in tests:
            cur_test = cur.adj(test_direc)
            nxt_test = nxt.adj(test_direc)
            if _is_valid(cur_test) and _is_valid(nxt_test):
                _table[cur_test.x][cur_test.y].visit = True
                _table[nxt_test.x][nxt_test.y].visit = True
                path.insert(idx, test_direc)
                path.insert(idx + 2, Direc.opposite(test_direc))
                extended = True
                break
        if not extended:
            cur = nxt
            idx += 1
            if idx >= len(path):
                break
    return path

