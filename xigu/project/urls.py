from django.urls import path
from . import response


# info/list?page=<int:pageId>
# info/<int:projectId>/?phone=1234567
urlpatterns = [
    path('list', response.get_list),
    path('detail', response.get_detail),
    #path('project/<int:projectId>/', response.get_basic_info),
    #path('project-detail/<int:projectId>/', response.get_detail_info),
    #path('videos', response.get_video_list),
    #path('gen-qrcode/project', response.gen_QR_code_project),
    #path('gen-qrcode/opencourse', response.gen_QR_code_opencourse),
]