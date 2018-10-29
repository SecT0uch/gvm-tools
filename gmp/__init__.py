# -*- coding: utf-8 -*-
# Copyright (C) 2018 Greenbone Networks GmbH
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
Main module of gvm-tools.

This module exposes the main entry to gvm-tools.
The provided Gmp class implements the current stable `Greenbone Management
Protocol`_.

For details about the possible supported protocol versions please take a look at
:py:mod:`gmp.protocol`.

.. _Greenbone Management Protocol:
    https://docs.greenbone.net/API/GMP/gmp.html
"""
from gmp.protocol.v7 import Gmp

VERSION = (2, 0, 0, 'dev', 1)

def get_version():
    """Returns the version of gvm-tools as a string in `PEP440`_ compliant
    format.

    Returns:
        str: Current version of gvm-tools

    .. _PEP440:
       https://www.python.org/dev/peps/pep-0440
    """
    if len(VERSION) > 3:
        version = '.'.join(str(x) for x in VERSION[:4])
        version += str(VERSION[4])
    else:
        version = '.'.join(str(x) for x in VERSION)
    return version
