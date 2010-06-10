# -*- coding: utf-8 -*-
"""
$Id$

Copyright 2008-2009 Lode Leroy

This file is part of PyCAM.

PyCAM is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

PyCAM is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with PyCAM.  If not, see <http://www.gnu.org/licenses/>.
"""

from pycam.Geometry import Triangle, Line, Point
from pycam.Geometry.Model import Model

def TestModel():
    points = []
    points.append(Point(-2,1,4))
    points.append(Point(2,1,4))
    points.append(Point(0,-2,4))
    points.append(Point(-5,2,2))
    points.append(Point(-1,3,2))
    points.append(Point(5,2,2))
    points.append(Point(4,-1,2))
    points.append(Point(2,-4,2))
    points.append(Point(-2,-4,2))
    points.append(Point(-3,-2,2))

    lines = []
    lines.append(Line(points[0],points[1]))
    lines.append(Line(points[1],points[2]))
    lines.append(Line(points[2],points[0]))
    lines.append(Line(points[0],points[3]))
    lines.append(Line(points[3],points[4]))
    lines.append(Line(points[4],points[0]))
    lines.append(Line(points[4],points[1]))
    lines.append(Line(points[4],points[5]))
    lines.append(Line(points[5],points[1]))
    lines.append(Line(points[5],points[6]))
    lines.append(Line(points[6],points[1]))
    lines.append(Line(points[6],points[2]))
    lines.append(Line(points[6],points[7]))
    lines.append(Line(points[7],points[2]))
    lines.append(Line(points[7],points[8]))
    lines.append(Line(points[8],points[2]))
    lines.append(Line(points[8],points[9]))
    lines.append(Line(points[9],points[2]))
    lines.append(Line(points[9],points[0]))
    lines.append(Line(points[9],points[3]))

    model = Model()
    model.append(Triangle(points[0],points[1],points[2],lines[0],lines[1],lines[2]))
    model.append(Triangle(points[0],points[3],points[4],lines[3],lines[4],lines[5]))
    model.append(Triangle(points[0],points[4],points[1],lines[5],lines[6],lines[0]))
    model.append(Triangle(points[1],points[4],points[5],lines[6],lines[7],lines[8]))
    model.append(Triangle(points[1],points[5],points[6],lines[8],lines[9],lines[10]))
    model.append(Triangle(points[1],points[6],points[2],lines[10],lines[11],lines[1]))
    model.append(Triangle(points[2],points[6],points[7],lines[11],lines[12],lines[13]))
    model.append(Triangle(points[2],points[7],points[8],lines[13],lines[14],lines[15]))
    model.append(Triangle(points[2],points[8],points[9],lines[15],lines[16],lines[17]))
    model.append(Triangle(points[2],points[9],points[0],lines[17],lines[18],lines[2]))
    model.append(Triangle(points[0],points[9],points[3],lines[18],lines[19],lines[3]))
    return model

