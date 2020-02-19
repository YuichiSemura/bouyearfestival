from flask import *
import json
import random, string

import logging
import os
import datetime

from app_config import AppConfig
from authentification import Authentificater
from user_status import UserStatus
from startup import start_up
from constants import *
from forms.login_form import *
from forms.user_form import *
from forms.admin_form import *
from flask_wtf.csrf import CSRFProtect

current_dir = os.path.dirname(__file__)

# load configure file
app_config = AppConfig(os.path.join(current_dir, "app.conf"), current_dir)

# set ac for RSA
ac = Authentificater(app_config.get_sec_path(),
                     app_config.get_pub_path())

# Flask load
app = Flask(__name__)

# startup
start_up(app, app_config)
#csrf = CSRFProtect(app)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(app.root_path, 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/start", methods=["GET"])
def start():
    q1, q2, q3, parity = get_cookie()
    if (q1 is None) or (q2 is None) or (q3 is None) or (parity is None):
        # initiarize
        q1, q2, q3 = 0, 0, 0
        status = UserStatus(0, 0, 0)
        parity = ac.make_sign(status.to_string())

    # when cheating
    if not check_parity(q1, q2, q3, parity):
        return redirect("/final")

    form = LoginForm()
    #responsing handling
    response = None
    if q1 == 1 and q2 == 1 and q3 == 1:
        response = make_response(render_template(LOGIN_PAGE, form=form, is_after=1, 
                                                angel_msg = MSG_s2))
    else:
        response = make_response(render_template(LOGIN_PAGE, form=form, 
                                                angel_msg = MSG_s1))

    set_cookie(response, q1, q2, q3, parity)
    return response

@app.route("/persons", methods=["GET"])
def persons():
    persons_dict = json.loads(PERSONS_JSON)
    response = make_response(render_template("persons.html", persons_dict=persons_dict))
    return response

@app.route("/restart", methods=["GET"])
def restart():
    q1, q2, q3 = 0, 0, 0
    status = UserStatus(0, 0, 0)
    parity = ac.make_sign(status.to_string())
    form = LoginForm()
    response = make_response(render_template(LOGIN_PAGE, form=form, 
                                                angel_msg = MSG_s1))
    set_cookie(response, q1, q2, q3, parity)
    return response

@app.route("/post_p1", methods=["POST"])
def post_p1():
    
    q1, q2, q3, parity = get_cookie()
    # when cheating
    if not check_parity(q1, q2, q3, parity):
        return redirect("/final")

    form = LoginForm()

    answer = request.form["answer"]
    response = None
    
    if not form.validate_on_submit():
        if q1 == 1 and q2 == 1 and q3 == 1:
            angel_msg = MSG_w29
            response = make_response(render_template(LOGIN_PAGE, form=form,
                            angel_msg=angel_msg,
                            is_after=1))
        else:
            angel_msg = MSG_w19
            response = make_response( render_template(LOGIN_PAGE, form=form,
                            angel_msg=angel_msg))
        set_cookie(response, q1, q2, q3, parity)
        
        return response

    # render page
    if answer == ANS1:
        # when muraseyuichi
        user_form = UserForm()
        angel_msg = MSG_s3
        response = make_response(render_template(murase_PAGE, form=user_form, user=ANS1,
                            angel_msg=angel_msg))
        q1 = 1
        status = UserStatus(q1, q2, q3)
        parity = ac.make_sign(status.to_string())
    elif answer == ANS3:
        # when tanakayuichi
        admin_form = AdminForm()
        response = make_response(render_template(tanaka_PAGE, form=admin_form))
    elif answer == WRGANS11:
        # when muraseyuuichi
        angel_msg = MSG_w11
        response = make_response(render_template(LOGIN_PAGE, form=form,
                            angel_msg=angel_msg))
    
    # 2kaime
    elif answer == ANS3 and q1 == 1 and q2 == 1 and q3 == 1:
        # when tanakayuichi
        admin_form = AdminForm()
        response = make_response(render_template(tanaka_PAGE, form=admin_form))
    
    elif answer == YUICHI and q1 == 1 and q2 == 1 and q3 == 1:
        # when yuichi
        angel_msg = MSG_w21
        err_msg = ERR2
        response = make_response(render_template(LOGIN_PAGE, form=form,
                            is_after=1,
                            err_msg=err_msg,
                            angel_msg=angel_msg))

    elif q1 == 1 and q2 == 1 and q3 == 1:
        # when wrong
        err_msg = ERR2
        angel_msg = MSG_w29
        response = make_response(render_template(LOGIN_PAGE, form=form,
                            is_after=1,
                            err_msg=err_msg,
                            angel_msg=angel_msg))
    else:
        # when wrong
        err_msg = ERR2
        angel_msg = MSG_w19
        response = make_response(
            render_template(LOGIN_PAGE, form=form,
                            err_msg=err_msg,
                            angel_msg=angel_msg))
        
    set_cookie(response, q1, q2, q3, parity)
    
    return response

@app.route("/post_p2", methods=["POST"])
def post_p2():
    q1, q2, q3, parity = get_cookie()
    # when cheating
    if not check_parity(q1, q2, q3, parity):
        return redirect("/final")

    form = UserForm()
    
    answer = request.form["answer2"]
    response = None

    if not form.validate_on_submit():
        angel_msg = MSG_w39
        response = make_response(render_template(murase_PAGE, form=form, user=ANS1,
                            angel_msg=angel_msg))
        set_cookie(response, q1, q2, q3, parity)
        return response
    
    # render page
    if q1 == 1 and answer == ANS2:
        err_msg = ERR7
        angel_msg = MSG_s4
        response = make_response(
            render_template(murase_PAGE, form=form, user=ANS1,
                            is_after=1,
                            angel_msg=angel_msg,
                            err_msg=err_msg))
        q2 = 1
        q3 = 1
        status = UserStatus(q1, q2, q3)
        parity = ac.make_sign(status.to_string())

    else:
        err_msg = ERR6
        angel_msg = MSG_w39
        response = make_response(
            render_template(murase_PAGE, form=form,
                            angel_msg=angel_msg,
                            err_msg=err_msg))
        
    set_cookie(response, q1, q2, q3, parity)
    
    return response

@app.route("/post_p3", methods=["POST"])
def post_p3():
    q1, q2, q3, parity = get_cookie()
    # when cheating
    if not check_parity(q1, q2, q3, parity):
        return redirect("/final")

    form = AdminForm()

    answer = request.form["answer3"]
    response = None
    
    if answer == ANS2 and q1 == 1:
        now = datetime.datetime.now()
        datestr = now.strftime("%H:%M:%S")
        response = make_response(
            render_template(tanaka_PAGE, form=form, success=1, datestr=datestr))
    else:
        err_msg = ERR6
        response = make_response(
            render_template(tanaka_PAGE, form=form, err_msg=err_msg))

    set_cookie(response, q1, q2, q3, parity)
    return response

@app.route("/final", methods=["GET"])
def final():
    response = make_response(render_template(DUMMY_PAGE))
    status = UserStatus(0, 0, 0)
    parity = ac.make_sign(status.to_string())
    set_cookie(response, 0, 0, 0, parity)
    return response

"""
@app.errorhandler(Exception)
def handle_global_error(e):
    # TODO: make redirection page
    logging.exception(e)
    return redirect("/restart")
"""

def get_cookie():
    q1 = request.cookies.get(COOKIE_Q1)
    q1 = None if q1 is None else int(q1)
    q2 = request.cookies.get(COOKIE_Q2)
    q2 = None if q2 is None else int(q2)
    q3 = request.cookies.get(COOKIE_Q3)
    q3 = None if q3 is None else int(q3)
    parity = request.cookies.get(COOKIE_PARITY)
    parity = None if parity is None else bytes.fromhex(parity)
    return q1, q2, q3, parity

def set_cookie(response, q1, q2, q3, parity):
    response.set_cookie(COOKIE_Q1, value=str(q1))
    response.set_cookie(COOKIE_Q2, value=str(q2))
    response.set_cookie(COOKIE_Q3, value=str(q3))
    response.set_cookie(COOKIE_PARITY, value=str(parity.hex()))

def check_parity(q1, q2, q3, parity):
    # check parity
    b = ac.verify(UserStatus(q1, q2, q3).to_string(), parity)
    return b

if __name__ == '__main__':
    # set up user status
    randlst = [random.choice(string.ascii_letters + string.digits) for i in range(100)]
    s = ''.join(randlst)
    UserStatus.random_str = s
    # set up app
    app.debug = True
    app.logger.setLevel(logging.DEBUG)
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))
    #app.run()


