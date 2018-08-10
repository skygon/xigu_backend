# -*- coding: utf-8 -*-
import nexmo
import random
import json
import sys
import os
from aliyunsdkdysmsapi.request.v20170525 import SendSmsRequest
from aliyunsdkdysmsapi.request.v20170525 import QuerySendDetailsRequest
from aliyunsdkcore.client import AcsClient
import uuid
from aliyunsdkcore.profile import region_provider
from aliyunsdkcore.http import method_type as MT
from aliyunsdkcore.http import format_type as FT

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
from xigu_utils import utils

try:
    reload(sys)
    sys.setdefaultencoding('utf8')
except NameError:
    pass
except Exception as err:
    raise err

# !!! DO NOT MODIFY NEXMO keys
NEXMO_API_KEY = 'c031e686'
NEXMO_API_SECRET = '8d6fb85490b5c812'

# !!! DO NOT MODIFY aliyun keys
REGION = "cn-hangzhou"
PRODUCT_NAME = "Dysmsapi"
DOMAIN = "dysmsapi.aliyuncs.com"
ACCESS_KEY_ID = "HfUcPucMgQEWgNXI"
ACCESS_KEY_SECRET = "mz99jike788kX4tkB8C5Pb5cGepR3j"

acs_client = AcsClient(ACCESS_KEY_ID, ACCESS_KEY_SECRET, REGION)
region_provider.add_endpoint(PRODUCT_NAME, REGION, DOMAIN)


def get_verify_code():
    return random.randint(1000, 9999)


def sms_to_cn(business_id, phone_numbers, sign_name, template_code, template_param=None):
    smsRequest = SendSmsRequest.SendSmsRequest()
    # 申请的短信模板编码,必填
    smsRequest.set_TemplateCode(template_code)

    # 短信模板变量参数
    if template_param is not None:
        smsRequest.set_TemplateParam(template_param)

    # 设置业务请求流水号，必填。
    smsRequest.set_OutId(business_id)

    # 短信签名
    smsRequest.set_SignName(sign_name)
	
    # 数据提交方式
	# smsRequest.set_method(MT.POST)
	
	# 数据提交格式
    # smsRequest.set_accept_format(FT.JSON)
	
    # 短信发送的号码列表，必填。
    smsRequest.set_PhoneNumbers(phone_numbers)

    # 调用短信发送接口，返回json
    smsResponse = acs_client.do_action_with_exception(smsRequest)

    # TODO 业务处理

    return smsResponse



def sms_to_us(phone_num, msg):
    client = nexmo.Client(key=NEXMO_API_KEY, secret=NEXMO_API_SECRET)
    response = client.send_message({'from': '12015471485', 'to': phone_num, 'text': msg})

    response = response['messages'][0]
    if response['status'] == '0':
        utils.logger.debug('Send sms success. Remaining balance is %s', response['remaining-balance'])
    else:
        utils.logger.debug(response['error-text'])


if __name__ == "__main__":
    # msg = 'verification code: %s. Valid for 5 minutes. [Fang88.com]' %(get_verify_code())
    msg = 'test sms'
    phone_num = '2024569713' # test phone number
    sms_to_us(phone_num,msg)

    # send to cn
    __business_id = uuid.uuid1()
    params = {}
    params['code'] = '12345'
    print(sms_to_cn(__business_id, "13858093509", "房88", "SMS_101290035", json.dumps(params)))