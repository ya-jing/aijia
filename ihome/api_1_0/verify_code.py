# coding:utf-8

from . import api
from ihome.utils.captcha.captcha import captcha
from ihome import redis_store, constants
from flask import current_app, jsonify, make_response
from ihome.utils.response_code import RET

# GET 127.0.0.1/api/v1.0/image_codes/<image_code_id>

@api.route("/image_codes/<image_code_id>")
def get_image_code(image_code_id):
    """
    获取图片验证码
    :param image_code_id :图片验证码编号
    :return:若果出现异常，返回异常信息，否则，返回验证码图片
    """
    # 业务逻辑处理
    # 生成验证码图片
    # 名字，真实文本，图片数据
    name,text,image_data=captcha.generate_captcha()

    # 将编号以及验证码真实值保存到redis（选择字符串）中,设置有效期（自定义）
    # redis_store.set('iamge_code_%s'%image_code_id,text)
    # redis_store.expire('image_code_%s' % image_code_id, constants.IMAGE_CODE_REDIS_EXPIRES)
    # redis:字符串 列表 哈希 set
    # "key":xxx
    # image_codes":{"编号1"："真实文本"}哈希类型
    # 返回图片
    # 将以上合并写
    try:
        redis_store.setex('image_code_%s' %image_code_id,constants.IMAGE_CODE_REDIS_EXPIRES,text)
    except Exception as e:
        # 记录日记
        current_app.logger.error(e)
        # # return jsonify(errno=RET.DBERR, errmsg="save image code failed")
        # 出现异常，返回json格式的提示
        return jsonify(errno=RET.DBERR,errmsg='保存图片验证码失败')

    # 没有异常 返回验证码图片，并指定一下Content-Type(默认为test/html)类型为image,不改不认识图片
    resp = make_response(image_data)
    resp.headers['Content-Type'] = 'image/jpg'
    return resp

