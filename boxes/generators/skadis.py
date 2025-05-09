# Copyright (C) 2013-2016 Florian Festi
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

from boxes import *


class SkadisBoard(Boxes):
    """Customizable Ikea like pegboard"""

    description = """Best cut from 5mm material to match the original. Use the included washers to mount. The board needs space towards the wall for hooks to go into.

You can use boxes and holders from the "WallMounted" group with "skadis" as "walltype". Note that these generators do not have any support to pick the right width(s). Inner distance between slots are 35 + n * 40 mm. It is recommended to cut the acceessories from 4 mm material. Then 36 + n * 40 mm should be used for inner widths. Deselect "outside" where available to be able to deal with inner measurements."""

    ui_group = "WallMounted"

    def __init__(self) -> None:
        Boxes.__init__(self)

        self.argparser.add_argument(
            "--columns",  action="store", type=int, default=17,
            help="Number of holes left to right counting both even and odd rows")
        self.argparser.add_argument(
            "--rows",  action="store", type=int, default=27,
            help="Number of rows of holes top to bottom")


    def CB(self):
        for r in range(self.rows):
            for c in range(self.columns):
                if (r+c) % 2 == 0:
                    continue
                self.rectangularHole((c+1)*20 - 8, (r+1)*20, 5, 15, r=2.5)

    def render(self):
        self.roundedPlate((self.columns+1) * 20, (self.rows+1)*20, edge="e", r=8,
                          extend_corners=False, callback=[self.CB], move="up")
        self.partsMatrix(8, 4, "up", self.parts.disc, 15, 5)
