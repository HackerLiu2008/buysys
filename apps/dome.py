# 以下是自用零时接口,/dome

from flask import request, jsonify
from . import dome_blueprint
import time
from tools_me.send_sms.send_sms import CCP


@dome_blueprint.route('/send_sms', methods=['GET'])
def lum_change():
    phone = request.args.get('phone')
    user_name = request.args.get('userName')
    account = request.args.get('account')
    key = request.args.get('key')
    t = time.time() + 10
    if t < float(key):
        return jsonify({'code': 404, 'msg': '超出范围时间!'})
    send = CCP()
    res = send.send_Template_sms(int(phone), [user_name, account], 476165)
    return jsonify({'code': res, 'msg': ''})
