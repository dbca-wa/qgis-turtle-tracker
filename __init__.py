# -*- coding: utf-8 -*-
"""
/***************************************************************************
 TurtleTracker
                                 A QGIS plugin
 Turtle track capture from aerial images
                             -------------------
        begin                : 2017-04-18
        copyright            : (C) 2017 by Dept Parks & Wildlife WA
        email                : florian.mayer@dpaw.wa.gov.au
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load TurtleTracker class from file TurtleTracker.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .turtle_tracker import TurtleTracker
    return TurtleTracker(iface)
