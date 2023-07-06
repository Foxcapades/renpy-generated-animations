init python:
    def generate_animation(directory, fps = 30, looping = False, hold_last = False):
        """
        Generates an animation from the png files in the given directory, in
        name order.  It is advised that, to keep the ordering of frames correct,
        the files in the given directory have a common name suffixed with an
        incrementing integer.  For example:
        [ file01.png, file02.png, file03.png, ... ].

        Parameters:
        directory (str): The directory containing the animation frames.  This
        path is relative to the root of the game project.  For example, a path
        may look like: "images/animations/explosion".

        fps (int): Frames per second for the animation.

        looping (bool): Whether or not the animation should loop.

        hold_last (bool): Whether or not the animation should hold on the last
        frame or vanish after completion.

        Returns:
        str: Name of the generated animation.
        """
        from uuid import uuid4

        # List to hold the animation components.  This list contains non-tuple
        # pairs of images and pause durations.  For example:
        # [ image, pause, image, pause, image, pause ]
        animation_parts = []

        # Divide 1 "second" by the target FPS to get the pause duration.
        pause = 1.0/fps

        # Build the list of animation components.  This is done by iterating
        # through the files known to renpy and...
        for path in renpy.list_files():
            # filtering down to only those files that start with the target
            # directory path, then...
            if path.startswith(directory):

                # make sure the file extension is "png".
                if path[path.rindex(".")+1:].lower() == "png":
                    # If the extension is "png" then add the file to the
                    # animation
                    animation_parts.append(path)
                    # followed by the pause for that animation frame
                    animation_parts.append(pause)
        
        # If we don't want the animation to loop
        if not looping:
            # And we don't want to hold on the last frame.
            if not hold_last:
                # end the animation with a clear frame (with no following duration).
                renpy.image("clear_solid_last_animation_frame", Solid("#ffffff00"))
                animation_parts.append("clear_solid_last_animation_frame")
            # And we _do_ want to hold on the last frame
            else:
                # remove the last pause duration item from the animation_parts
                # list to set the last frame to have no set pause duration
                animation_parts.pop()

        # Generate a "random" value for the "name" of the animation. This should
        # not be referenced by human written code so the value doesn't actually
        # matter as long as it is unique.
        image_name = str(uuid4())

        # Generate a new image for our animation
        renpy.image(image_name, Animation(*animation_parts))

        # And return its name.
        return image_name

image explosion = generate_animation("images/effects/explosion", 45, False, False)
