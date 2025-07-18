def validateCoordinate(coord): # ex) coord = [1, 5]
    for coor in coord:
        if coor > 5 or coor < -5: # invalid coord
            return False
    return True

def move(dir, coord): # ex) dir = 'U', coord = [1, 5]
    nx, ny = coord
    if dir=='U': # up
        ny += 1
    elif dir=='D': # down
        ny -= 1
    elif dir=='R': # right
        nx += 1
    elif dir=='L': # left
        nx -= 1
    if validateCoordinate([nx, ny]): # valid
        return [nx, ny]
    else: # invalid
        return coord

def solution(dirs):
    coord = [0, 0]
    route = set()
    
    for dir in dirs:
        nextCoord = move(dir, coord)
        if nextCoord != coord:
            # route.add((*coord, *nextCoord))
            route.add(tuple(sorted([tuple(coord), tuple(nextCoord)])))
            coord = nextCoord
        
    answer = len(route)
    
    return answer
