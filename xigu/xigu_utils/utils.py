import os
import logging
from django.http import HttpResponse, JsonResponse
from django.conf import settings

import redis
import urllib
import urllib.parse
import urllib.request
import json
import datetime

logger = logging.getLogger('app_debug')

site = "https://api2.fang88.com"
'''
CAUTION: DO NOT make cycle dependencies
oss2util -> utils
ffmpeg_utils -> utils
vodutil -> utils
model_util -> utils | oss2util | ffmpeg_utils
'''

'''
CREATE TABLE `project_visit` (
  `project_id` int(11) NOT NULL,
  `date_str` char(10) DEFAULT NULL,
  `page_visit_count` int(11) DEFAULT NULL,
  UNIQUE KEY `uq_pid_count` (`project_id`,`date_str`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8
'''

# OSS account info. 
clientId = 'HfUcPucMgQEWgNXI'
clientSecret = 'mz99jike788kX4tkB8C5Pb5cGepR3j'

# project types
FUND = 1
REAL_ESTATE = 2
COMMERCIAL_ESTATE = 3
INSURANCE = 4

# file name to md5 file name
original_name = {}

# audio base dir
AUDIO_BASE_DIR = os.path.join(settings.MEDIA_ROOT, 'upload', 'audio')

# global redis connection
g_redis = redis.Redis('127.0.0.1', 6379)
md5_to_name = 'md5_to_name'
wx_token = 'wx_token'

# ================ REDIS OPERATIONS ============================
def set_key(k, v):
    try:
        g_redis.set(k, v)
    except Exception as e:
        logger.error('redis set key fail: %s', str(e))

def get_key(k):
    try:
        g_redis.get(k)
    except Exception as e:
        logger.error('redis get key fail: %s', str(e))

def save_to_redis(k, v):
    try:
        g_redis.hset(md5_to_name, k, v)
    except Exception as e:
        logger.error('save [%s : %s] to redis fail', k, v)


def get_from_redis(k):
    try:
        return g_redis.hget(md5_to_name, k).decode('utf-8')
    except Exception as e:
        return None

# HINCRBY 'project_visit' '2018-06-01' 1
# set daliy table expire time to 25 hours 72*3600 = 259200, like expire '2018-06-01' 259200
#

# date_str is composed by date and mysql table name, like '2018-06-01#project_visit', '2018-06-01#open_course_visit'
def incr_visit_count_table(item_type, item_id, count):
    try:
        # get date string as '2018-06-01'
        date_str = datetime.datetime.now().strftime("%Y-%m-%d")
        if item_type == "project":
            date_str = date_str + "#project_visit"
        elif item_type == "audio":
            date_str = date_str + "#open_course_visit"
        elif item_type == "video":
            date_str = date_str + "#video_visit"
        
        g_redis.hincrby(date_str, item_id, count)
    except Exception as e:
        raise e


# ================ END REDIS ========================================


# helper functions to return success or error wrapper
def return_error(err_code):
    data = {}
    data['status'] = err_code
    return JsonResponse(data, safe=False)

def return_success(data, count=None):
    res = {}
    res['status'] = 200
    res['data'] = data
    if count is not None:
        res['total_count'] = count
    return JsonResponse(res, safe=False)



if __name__ == '__main__':
    name = get_from_redis("9afc89d2907efd243869213d2124e51a.jpg")
    print(name)
    print(type(name))
