from django.urls import path
from django.conf.urls import url
from . import response, views

# code?<mobile=xxx>
# checkcode (POST params: {'code': xxx, 'mobile': xxx})
urlpatterns = [
    path('proposal', response.send_proposal),
    path('submitproposal', response.receive_proposal),
]