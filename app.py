#!/usr/bin/env python

import os
from bottle import route, run, static_file, template, post
from __init__ import get_ssids

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
def hello():
       return template('main1.tpl', List1=get_ssids())

@post("/")
def connect():

    if request.POST.get("sub_OPEN","").strip():
        mSSID = request.forms.get('fSSID_OPEN')
        connect_to_network(mSSID)
        redirect("/load")

    elif request.POST.get("sub_WPA","").strip():
        password = request.forms.get('pwd2')
        if password == 'abcd':
            mSSID = request.forms.get('fSSID_WPA')
            connect_to_network(mSSID)
            redirect("/load")
        else:
            return template('main1.tpl', List1=get_ssids())

    elif request.POST.get("sub_WEP","").strip():
        password = request.forms.get('pwd1')
        if password == 'abcd':
            mSSID = request.forms.get('fSSID_WEP')
            connect_to_network(mSSID)
            redirect("/load")
        else:
            return template('main1.tpl', List1=get_ssids())

    redirect("/")


#Put new template in the if    statements above when checking password.
@route("/debug")
def debug():

    return template('debug1.tpl')



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    run(host='localhost', port=port)
