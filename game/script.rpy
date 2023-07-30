image explosion = generate_animation("images/effects/explosion", fps=45)

label start:
    "What's this?"

    show explosion:
        zoom 2.5
        xpos 600
        ypos 70

    "Oh shit! An explosion!"

    hide explosion

    return
