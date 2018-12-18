from expand import expand
import queue as Qu

class Entry(object):
    def __init__(self, location, path, h, g):
        self.location = location
        self.path = []
        self.path = path
        self.h = h
        self.g = g
        self.f = h + g

def a_star_search (dis_map, time_map, start, end):
    path = []
    # TODO Put your code here.
    # be sure to call the imported function expand to get the next list of nodes
    locations = dis_map.keys()  # Checks if the locations passed in are in the map
    if start not in locations or end not in locations:
        return []
    currentPath = []
    closed = []
    currentPath.append(start)
    q = Qu.PriorityQueue()
    currentLoc = start
    currentDist = 0
    found = 0
    # open = 0   #  used to track number of opened nodes
    while currentLoc != end and found == 0:
        if currentLoc not in closed:
            next = expand(currentLoc, time_map)
            closed.append(currentLoc)
            # open += 1
            if next:  # if not dead end
                for i in next:  # For each next location
                    try:
                        h = dis_map[i][end]
                        g = currentDist + time_map[currentLoc][i]
                        f = int(h + g)
                        newEntry = Entry(i, currentPath + [i], h, g)
                        q.put((f, i, newEntry))
                    except KeyError:
                        print('Locations in Time Map and Distance Map are incompatible.')
        if not q.empty():
            nextQueue= q.get()[2]
            currentLoc = nextQueue.location
            currentDist = nextQueue.g
            currentPath = nextQueue.path
        else:
            currentPath=[]
            found = 1
    path = currentPath
    return path


