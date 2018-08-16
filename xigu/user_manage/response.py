import requests
from django.http import HttpResponse, JsonResponse
import sys
import os
import json
import uuid
import hashlib
import random
from .models import User
sys.path.append(os.path.join(os.path.dirname(__file__)))
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))
from xigu_utils import utils, smsutil
from project.models import Project
from project.response import collect_project_info, get_yearly_return

# An in-memory dict used to stored phone number mapped to current verify code
phone_verify_code = {}

def send(type, phone_num):
    code = smsutil.get_verify_code()
    # store code in memory
    phone_verify_code[phone_num] = code
    utils.logger.debug('code[%s] sent to phone[%s]', code, phone_num)
    if type == 'cn':
        __business_id = uuid.uuid1()
        params = {}
        params['code'] = code
        smsutil.sms_to_cn(__business_id, phone_num, "房88", "SMS_101290035", json.dumps(params))
    else:
        msg = 'verification code: %s. Valid for 5 minutes. [Fang88.com]' %(code)
        smsutil.sms_to_us(phone_num, msg)


def send_verify_code(request):
    try:
        phoneNumber = request.GET.get('mobile')
        # check phone, cn or us
        type = 'cn'
        # TODO if front-end not verify the phone number, back-end will verify again
        if len(phoneNumber) == 11:
            type = 'cn'
        elif len(phoneNumber) == 10:
            type = 'us'
        else:
            type = 'unknown'
        
        utils.logger.debug('type is %s', type)
        if type == 'unknown':
            return utils.return_error(400)
        # send msg
        send(type, phoneNumber)

        # return http response
        return utils.return_success({})
    except Exception as e:
        utils.logger.debug("send verify code fail: %s", str(e))
        return utils.return_error(400)


def check_verify_code(request):
    try:
        utils.logger.debug('check verification post body: %s', request.POST)
        phone_num = request.POST.get('mobile')
        recv_code = request.POST.get('code')
        send_code = phone_verify_code.get(phone_num)

        utils.logger.debug('phone number: %s, code: %s', phone_num, recv_code)
        if send_code is not None and send_code == int(recv_code):
            if User.objects.filter(mobile=phone_num).exists() is False:
                # create a new user object for current phone number
                new_uobj = User.objects.create()
                new_uobj.mobile = phone_num
                new_uobj.save()
            else:
                uobj = User.objects.get(mobile=phone_num)
                uobj.save() # just for update active time
            
            return utils.return_success({})
        else:
           return utils.return_error(403)
            #return HttpResponse(403)
    except Exception as e:
        utils.logger.debug('check verification fail: %s', str(e))
        return utils.return_error(400)

def follow(request):
    try:
        phone_num = request.POST.get('mobile')
        pid = request.POST.get('project_id')

        utils.logger.debug('user[%s] follows project[id: %s]', phone_num, pid)
        uobj = User.objects.get(mobile=phone_num)
        pobj = Project.objects.get(id=pid)
        
        # add relation ship
        uobj.follow_projects.add(pobj)

        return utils.return_success({})
    except Exception as e:
        utils.logger.debug('follow fail: %s', str(e))
        return utils.return_error(400)

def unfollow(request):
    try:
        phone_num = request.POST.get('mobile')
        pid = request.POST.get('project_id')

        utils.logger.debug('user[%s] unfollows project[id: %s]', phone_num, pid)
        uobj = User.objects.get(mobile=phone_num)
        pobj = Project.objects.get(id=pid)
        
        # add relation ship
        uobj.follow_projects.remove(pobj)

        return utils.return_success({})
    except Exception as e:
        utils.logger.debug('unfollow fail: %s', str(e))
        return utils.return_error(400)

# get user info api
# userinfo/projects
def get_user_projects_info(request):
    try:
        page_id = request.POST.get('page')
        phone_num = request.POST.get('mobile')
        utils.logger.debug('user[%s] request projects info', phone_num)
        uobj = User.objects.get(mobile=phone_num)
        #followed_projects = uobj.follow_projects.all()
        
        total_count = uobj.follow_projects.count()
        # 10 projects for one page
        page_size = 10
        
        if page_id is None or int(page_id) < 0:
            page_id = 1

        full_info = {}

        # get followed projects
        projects_data = []
        
        start = (int(page_id) - 1) * page_size
        end = start + page_size
        #projects = followed_projects[start:end]

        # execute raw sql to get ordered follow projects
        sql = 'select project_id from user_follow_projects where user_id=%s order by id desc limit %s, %s'
        
        cursor = connection.cursor()
        cursor.execute(sql, [uobj.id, start, page_size])

        res = cursor.fetchone()
        utils.logger.debug('fetch user follow projects result %s', res)
        while res is not None:
            pid = res[0]
            p = Project.objects.get(id=pid)
            
            data = collect_project_info(p)
            
            data['follow'] = 1
            
            projects_data.append(data)
            res = cursor.fetchone()
        
        full_info['projects'] = projects_data
        return utils.return_success(full_info, total_count)
    except Exception as e:
        utils.logger.debug('get user projects info fail: %s', str(e))
        return utils.return_error(400)


def get_user_investments_info(request):
    try:
        page_id = request.POST.get('page')
        phone_num = request.POST.get('mobile')
        utils.logger.debug('user[%s] request projects info', phone_num)
        uobj = User.objects.get(mobile=phone_num)
        
        total_count = uobj.investment_set.count()
        
        # 10 projects for one page
        page_size = 10
        
        if page_id is None or int(page_id) < 0:
            page_id = 1
        
        start = (int(page_id) - 1) * page_size
        end = start + page_size

        all_invests = uobj.investment_set.all()[start:end]
        full_info = {}
        invests_data = []

        for invest in all_invests:
            data = {}
            data['estimate_yearly_return'] = get_yearly_return(invest.project)['yearly_return']
            data['principal'] = invest.principal
            data['interest'] = invest.interest
            invests_data.append(data)
        
        full_info['investments'] = invests_data
        return utils.return_success(full_info, total_count)
    except Exception as e:
        utils.logger.debug('get user investments info fail: %s', str(e))
        return utils.return_error(400)