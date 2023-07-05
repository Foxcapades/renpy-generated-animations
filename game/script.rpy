define e = Character("Eileen")

label start:
    scene bg room
    show eileen happy

    e "You've created a new Ren'Py game... Wait. What's this?"

    show explosion:
        zoom 2.0
        xpos 675
        ypos 70

    pause 0.5

    e "AHHHH!!  MY FACE! IT EXPLODED!"

    hide explosion

    return
