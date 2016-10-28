# -*- coding: utf-8 -*-
#
#    dummy_flask_server is used to test Archivematica and its callbacks.
#    Copyright (C) 2016  Rémi Ducceschi <remi.ducceschi@gmail.com>
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software Foundation,
#    Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301  USA

from distutils.core import setup


setup(
    name = "dummy_flask_server",
    packages = ["dummy_flask_server"],
    version = "0.1",
    description = "A small test for Archivematica callbacks",
    author = "Rémi Ducceschi",
    author_email = "remi.ducceschi@gmail.com",
    license = "GNU GPL v3.0",
    url = "https://github.com/remileduc/dummy_flask_server",
    platforms='any',
    install_requires=[
        "Flask"
    ]
)
