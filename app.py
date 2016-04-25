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
    return template('debug.tpl', check= "diagnostics", ssid=get_ssids())

@route("/networks")
def networks():
    return template('debug.tpl', check="networks", ssid=get_ssids(), pwdCheck="")

@post("/networks")
def connect():

    if request.POST.get("sub_OPEN","").strip():

        mSSID = request.forms.get('fOPEN')
        print "Connecting to SSID: ",mSSID
        connect_to_network(mSSID)
        return template('debug.tpl', check="connected to network", mSSID=mSSID)

    elif request.POST.get("sub_WPA", "").strip():

        password = request.forms.get('pwdWPA')

        if password == 'abcd':

            mSSID = request.forms.get('fWPA')
            print "Connecting to SSID: ",mSSID
            connect_to_network(mSSID)

            return template('debug.tpl', check="connected to network", mSSID=mSSID, pwdCheck = "")
            #tried try-except instead of define pwdCheck but the bottom of the form is cut off. Will look into later
        else:
            #should display invalid password try again

            return template ('debug.tpl',check="networks", pwdCheck="incorrect password",ssid=get_ssids())
            redirect("/networks")

    elif request.POST.get("sub_WEP","").strip():

        password = request.forms.get('pwdWEP')

        if password == 'abcd':

            mSSID = request.forms.get('fWEP')
            print "Connecting to SSID: ",mSSID
            connect_to_network(mSSID)

            return template('debug.tpl', check="connected to network", mSSID=mSSID, pwdCheck = "")
            #tried try-except instead of define pwdCheck but the bottom of the form is cut off. Will look into later
        else:
            #should display invalid password try again
            return template ('debug.tpl',check="networks", pwdCheck="incorrect password",ssid=get_ssids())
            redirect("/networks")


    redirect("/networks")

@route('/diagnostics')
def debug():
    pageset = "diagnostics"
    return template('debug.tpl', check= pageset)

@post('/diagnostics')
def do_command():
    command = request.forms.get('fCMD')
    print "Entered command:",command
    pageset = "diagnostics"
    return template('debug.tpl', check = pageset)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    run(host='localhost', port=port)
