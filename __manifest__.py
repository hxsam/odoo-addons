# -*- encoding: utf-8 -*-
##############################################################################
#
#    open2bizz
#    Copyright (C) 2016 open2bizz (open2bizz.nl).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name": "orbeon",
    "summary": 'Orbeon Forms integration interface',
    "description": 'Orbeon Forms integration interface',
    "version": "0.1",
    "author": "Open2bizz",
    "website": "http://www.open2bizz.nl",
    "license": "AGPL v3",
    "category": "Tools",
    "depends": ['document'],
    "data": [
        "security/res_groups.xml",
        "security/ir.model.access.csv",
        "views/orbeon_server.xml",
        "views/orbeon_builder.xml",
        "views/orbeon_runner.xml",
        "views/base.xml",
        ],
    "application": True,
    "installable": True,
}
