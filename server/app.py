#coding:utf-8

import time
import logging
from flask import Flask, request, jsonify
from config import *
from wxpay import WxPay, get_nonce_str, dict_to_xml, xml_to_dict


app = Flask(__name__)


@app.route('/')
def index():
    '''

    :return:
    '''
    return jsonify({'errcode': 0, 'errmsg': 'ok'})


@app.route('/wxpay/pay')
def create_pay():
    '''
    请求支付
    :return:
    '''
    data = {
        'appid': appid,
        'mch_id': mch_id,
        'nonce_str': get_nonce_str(),
        'body': '测试',                              # 商品描述
        'out_trade_no': str(int(time.time())),       # 商户订单号
        'total_fee': '1',
        'spbill_create_ip': spbill_create_ip,
        'notify_url': notify_url,
        'attach': '{"msg": "自定义数据"}',
        'trade_type': trade_type,
        'openid': '1111111111111111111111'
    }

    wxpay = WxPay(merchant_key, **data)
    pay_info = wxpay.get_pay_info()
    if pay_info:
        return jsonify(pay_info)
    return jsonify({'errcode': 40001, 'errmsg': '请求支付失败'})


@app.route('/wxpay/notify', methods=['POST'])
def wxpay():
    '''
    支付回调通知
    :return:
    '''
    if request.method == 'POST':
        logging.info(xml_to_dict(request.data))
        result_data = {
            'return_code': 'SUCCESS',
            'return_msg': 'OK'
        }
        return dict_to_xml(result_data), {'Content-Type': 'application/xml'}


if __name__ == '__main__':
    app.run(
        debug=True
    )
