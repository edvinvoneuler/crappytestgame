import Room as R

room_02 = R.Room("THIS ROOM IS FULL OF SNAKES! You died!", None, None, None,
                 "You hear hissing at the end of this corridor")

room_03 = R.Room("Congratulations, you found the treasure, you won!", None, None, None,
                 "A light shines at the end of this path")

room_04 = R.Room("This rooms seems to be a bedroom of a warrior, there's pieces of armor and other equipment strewn "
                 "about. You can see the covers heave as the warrior breaths, asleep in his bed", room_02, room_03,
                 None, "You hear snoring echoing from a unlit room.")

room_01 = R.Room("This is an empty room", room_02, room_03, room_04)

room_01.enter()
