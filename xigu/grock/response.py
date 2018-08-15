from django.core.mail import send_mail
import os
import sys
import json
import time
from django.conf import settings
from django.core.files.storage import Storage, default_storage
from django.core.files.base import ContentFile
sys.path.append(os.path.join(os.path.dirname(__file__)))
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))

from xigu_utils import utils, oss2util

def send_proposal(request):
    try:
        # send_mail的参数分别是  邮件标题，邮件内容，发件箱(settings.py中设置过的那个)，收件箱列表(可以发送给多个人),失败静默(若发送失败，报错提示我们)
        send_mail('Subject here', 'Here is the message.', 'cuiyun@fang88.me', ['cuiyun@fang88.me'], fail_silently=False)
        return utils.return_success({})
    except Exception as e:
        utils.logger.debug('send proposal fail: %s', str(e))
        return utils.return_error(400)

def send_email(data):
    try:
        message = '所属行业： ' + data['field'] + '\n'
        message += '融资情况： ' + data['invest'] + '\n'
        message += '公司注册情况： ' + data['register'] + '\n'
        message += '所需工位数量： ' + data['cubes'] + '\n'
        message += '联系电话： ' + data['mobile'] + '\n'
        message += 'BP链接： ' + data['oss_url'] + '\n' 
        send_mail('入驻申请', message, 'cuiyun@fang88.me', ['cuiyun@fang88.me'], fail_silently=False)
        return utils.return_success({})
    except Exception as e:
        utils.logger.debug('send email fail: %s', str(e))
        return utils.return_error(400)

def receive_proposal(request):
    try:
        utils.logger.debug('request is : %s', request.POST.get('data'))
        utils.logger.debug('request files is : %s', request.FILES)
        request_data = json.loads(request.POST.get('data'))
        utils.logger.debug('jsonfy request data is %s', request_data)
        
        data = {}
        data['field'] = request_data['field']
        data['invest'] = request_data['invest']
        data['register'] = request_data['register']
        data['cubes'] = request_data['cubes']
        data['mobile'] = request_data['mobile']
        bp_name = request_data['bp_name']
        utils.logger.debug('receive data is: %s', data)
        #bp_content = request.POST.get('bp_content')

        bp_content = request.FILES.get('files')
        utils.logger.debug('bp content is %s', bp_content)

        save_path = os.path.join(settings.MEDIA_ROOT, 'upload', bp_name)
        path = default_storage.save(save_path, ContentFile(bp_content.read()))

        utils.logger.debug('file saved to path: %s', path)

        # upload to oss cn
        target = 'grock_upload/' + oss2util.md5(path) + '.' + bp_name.split('.')[-1]
        oss2util.uploadFileCN(path, target)

        # send email
        oss_url = 'http://img.fang88.com/' + target
        data['oss_url'] = oss_url

        return send_email(data)
        #return utils.return_success({})
    except Exception as e:
        utils.logger.debug('receive proposal fail: %s', str(e))
        return utils.return_error(400)