################################################################################
## This file is licensed to you under the MPL 2.0 license.
## See the LICENSE file in the project root for more information.

screen journal():
    tag menu

    use game_menu(_("Journal"), scroll="viewport"):

        style_prefix "journal"

        has vbox:
            spacing 10

            for item in mp.journal:
                text item
