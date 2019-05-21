#!/usr/bin/env python3

import sys
import json
from bottle import route, run, redirect, static_file

from assets import AssetStore


# redirect to /versions
@route('/')
def index():
    redirect('/versions')


# return available versions
@route('/versions')
def versions():
    return json.dumps(store.tags())


# list assets for version
@route('/assets/<version>')
def assets(version):
    return json.dumps(store.list(version))


# returns a asset
@route('/assets/<version>/<name>')
def asset(version, name):
    path, fname = store.get(version, name)
    return static_file(fname, root=path)


store = AssetStore(sys.argv[1], sys.argv[2])

run(host='0.0.0.0', port=8080)
