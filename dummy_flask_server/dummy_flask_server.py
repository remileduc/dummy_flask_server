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

import sys

from datetime import datetime

from flask import Flask, request


app = Flask(__name__)
app.config.from_object("dummy_flask_server.config")

@app.route("/")
def index():
    return "Hello, World!"


@app.route("/error/")
def error():
    raise Exception()


@app.route("/pre-store/", methods=["GET", "POST"])
def start():
    app.config["START_TIME"] = datetime.now()
    return "", 200


@app.route("/post-store/", methods=["GET", "POST"])
def finish():
    raise Exception(request.values)


@app.route("/api/fixity/<uuid>", methods=["GET", "POST"])
def fixity(uuid):
    print >> sys.stderr, request.json
    return "", 201
