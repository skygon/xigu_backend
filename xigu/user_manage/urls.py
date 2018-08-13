from django.urls import path
from django.conf.urls import url
from . import response, views

# code?<mobile=xxx>
# checkcode (POST params: {'code': xxx, 'mobile': xxx})
urlpatterns = [
    path('code', response.send_verify_code),
    path('checkcode', response.check_verify_code),
    path('follow', response.follow),
    path('unfollow', response.unfollow),
    path('like', response.get_user_info),
]