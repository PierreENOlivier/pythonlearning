def clear_brush(brush):
    brush.clear()
    brush.penup()
    brush.home() # reset position, needs to have pen up otherwise draws
    brush.pendown()

def show_key(event):
    print(event.keysym)