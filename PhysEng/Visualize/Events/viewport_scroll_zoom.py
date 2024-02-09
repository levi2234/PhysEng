def viewport_scroll_zoom(viz, event):
        if event.button == 4:
            viz.simulationwidth = [viz.simulationwidth[0]-1, viz.simulationwidth[1]+1]
            viz.simulationheight = [viz.simulationheight[0]-1, viz.simulationheight[1]+1]
        if event.button == 5:
            viz.simulationwidth = [viz.simulationwidth[0]+1, viz.simulationwidth[1]-1]
            viz.simulationheight = [viz.simulationheight[0]+1, viz.simulationheight[1]-1]
    