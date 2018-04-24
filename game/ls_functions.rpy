################################################################################
## This file is licensed to you under the MPL 2.0 license.
## See the LICENSE file in the project root for more information.

init python:

    # Multi-game persitence data
    mp = MultiPersistent("barkpack.mp")

init:
    if not mp.journal:
        $ mp.journal = []

init -1 python:

    def journal_entry(item):
        if item not in mp.journal:
            mp.journal.append(item)

    ## Returns random dialog on each new game run.
    ## Though, technically it can be anything.
    ## Example: $ lalala = random_dialogue(["blablabla", "tatata", "lalala"])
    ## Based on https://lemmasoft.renai.us/forums/viewtopic.php?f=8&t=47341
    def random_dialogue(dialog_list):
        return renpy.random.choice(dialog_list)

    ## Pauses the game for brief second.
    ## By defualt this is 1.0, although it can be changed.
    def delay(dur = 1.0):
        renpy.pause(dur)

    ## Loads a song if it exists, and plays it.
    ## The purpose is to allow for soundtracks
    ## as optional content packs in order
    ## to avoid the obvious.
    def if_soundtrack(track, ply=True):
        if renpy.loadable(track):
            if ply is True:
                renpy.music.stop() # Substitute for queue support
                renpy.music.play(track)
            elif ply is False:
                renpy.music.stop()

    ## Check if the file exists and return the
    ## and return the file name if it does
    def get_file(file):
        if renpy.loadable(file):
            return file
