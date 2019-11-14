# 以下是自用零时接口,/dome

from flask import request, jsonify
from . import dome_blueprint
import time
from tools_me.send_sms.send_sms import CCP
import requests


@dome_blueprint.route('/send_sms', methods=['GET'])
def lum_change():
    phone = request.args.get('phone')
    user_name = request.args.get('userName')
    account = request.args.get('account')
    key = request.args.get('key')
    t = time.time() + 4
    if t < float(key):
        return jsonify({'code': 404, 'msg': '超出范围时间!'})
    send = CCP()
    res = send.send_Template_sms(int(phone), [user_name, account], 476970)
    return jsonify({'code': res, 'msg': ''})


@dome_blueprint.route('/luminati/', methods=['GET'])
def luminati():
    ip = request.args.get('ip')
    port = request.args.get('port')
    if not ip or not port:
        return '请填写IP和端口'
    url = "http://" + ip + ':22999/api/refresh_sessions/' + port
    resp = requests.post(url)
    code = resp.status_code
    print(code)
    if code == 204:
        return '切换成功!'
    else:
        return '切换失败请重试!'
