#!/usr/bin/env python

import os
from bottle import route, run, static_file
from bottle import template, get, post, request, redirect
from __init__ import get_ssids, connect_to_network

@route('/js/<filename>')
def js_static(filename):
    return static_file(filename, root='./js')

@route('/img/<filename>')
def img_static(filename):
    return static_file(filename, root='./img')

@route('/css/<filename>')
def img_static(filename):
    return static_file(filename, root='./css')

@route("/")
def main():
    pageset="diagnostics"
    return template('debug.tpl', check= pageset, ssid=get_ssids())

@route("/networks")
def networks():
    pageset="networks"
    return template('debug.tpl', check=pageset, ssid=get_ssids())

@post("/networks")
def connect():

    if request.POST.get("sub_OPEN","").strip():

        mSSID = request.forms.get('fOPEN')
        connect_to_network(mSSID)
        return '<h1 style="color:blue;">CONNECTED</h1>'

    elif request.POST.get("sub_WPA", "").strip():

        password = request.forms.get('pwdWPA')

        if password == 'abcd':

            mSSID = request.forms.get('fWPA')
            connect_to_network(mSSID)

            return '<h1 style="color:blue;">CONNECTED</h1>'
        else:
            #should display invalid password try again
            redirect("/")

    elif request.POST.get("sub_WEP","").strip():

        password = request.forms.get('pwdWEP')

        if password == 'abcd':

            mSSID = request.forms.get('fWEP')
            connect_to_network(mSSID)

            return '<h1 style="color:blue;">CONNECTED</h1>'
        else:
            #should display invalid password try again
            redirect("/")

    redirect("/")

@route('/diagnostics')
def debug():
    pageset = "diagnostics"
    return template('debug.tpl', check= pageset)

@post('/diagnostics')
def do_command():
    command = request.forms.get('fCMD')
    print "Testing command:",command
    pageset = "diagnostics"
    return template('debug.tpl', check = pageset)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    run(host='localhost', port=port)
