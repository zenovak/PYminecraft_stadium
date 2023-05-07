TOTAL_AREA = 50

# Builds the line
def _build_line(width: number, length: number, blockID: number):
    for index in range(width):
        for index2 in range(length):
            builder.move(FORWARD, 1)
            builder.place(blockID)
        builder.move(BACK, length)
        builder.move(LEFT, 1)

def builder_centre():
    builder.teleport_to_origin()
    builder.move(LEFT, 12)
    builder.move(FORWARD, 13)

def on_on_chat2():
    # The fields
    builder.move(LEFT, 12)
    builder.move(FORWARD, 13)
    shapes.circle(BROWN_WOOL, builder.position(), TOTAL_AREA, Axis.Y, ShapeOperation.REPLACE)
    
    builder.teleport_to_origin()    
    for j1 in range(7):
        _build_line(2, 24, GRASS)
        _build_line(2, 24, GREEN_WOOL)

    # the outlines
    builder.teleport_to_origin()
    builder.move(RIGHT, 1)
    for j2 in range(2):
        for i in range(25):
            builder.move(FORWARD, 1)
            builder.place(WOOL)
        builder.turn(LEFT_TURN)

        for i in range(29):
            builder.move(FORWARD, 1)
            builder.place(WOOL)
        builder.turn(LEFT_TURN)

    # Build the track lines
    builder.teleport_to_origin()
    builder.move(LEFT, 12)
    builder.move(FORWARD, 13)
    for i in range(0, 21, 3):
        shapes.circle(WHITE_CONCRETE, builder.position(), 24 + i, Axis.Y, ShapeOperation.OUTLINE)

    # The walls
    builder.teleport_to_origin()
    builder.move(LEFT, 12)
    builder.move(FORWARD, 13)
    for i in range(20):
        shapes.circle(WHITE_CONCRETE, builder.position(), TOTAL_AREA, Axis.Y, ShapeOperation.OUTLINE)
        builder.move(UP, 1)

    # seats
    builder_centre()
    builder.move(UP, 10)
    for i in range(7):
        builder.move(UP, 1)
        shapes.circle(OAK_WOOD_SLAB, builder.position(), 43 + i, Axis.Y, ShapeOperation.OUTLINE)

    # Dome
    builder_centre()
    builder.move(UP, 20)
    for i in range(0, 18):
        if (i < 15):
            builder.move(UP, 1)
        shapes.circle(GLASS, builder.position(), TOTAL_AREA - i, Axis.Y, ShapeOperation.OUTLINE)


player.on_chat("field", on_on_chat2)