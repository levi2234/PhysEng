
def xy_to_topygame(visualize,x,y):
    #scale any range to 0-screenwidth and 0-screenheight
    
    x = (x - visualize.simulationwidth[0]) * (visualize.screenwidth / (visualize.simulationwidth[1] - visualize.simulationwidth[0]))
    y = (y - visualize.simulationheight[0]) * (visualize.screenheight / (visualize.simulationheight[1] - visualize.simulationheight[0]))
    return (x, y)

