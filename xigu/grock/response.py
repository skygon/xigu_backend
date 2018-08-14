from django.core.mail import send_mail
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__)))
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))

from xigu_utils import utils

def send_proposal(request):
    try:
        # send_mail的参数分别是  邮件标题，邮件内容，发件箱(settings.py中设置过的那个)，收件箱列表(可以发送给多个人),失败静默(若发送失败，报错提示我们)
        send_mail('Subject here', 'Here is the message.', 'cuiyun@fang88.me', ['cuiyun@fang88.me'], fail_silently=False)
        return utils.return_success({})
    except Exception as e:
        utils.logger.debug('send proposal fail: %s', str(e))
        return utils.return_error(400)
