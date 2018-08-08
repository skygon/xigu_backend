from django.db import models
from django.utils.deconstruct import deconstructible
from django.core.files.storage import Storage, default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField
from DjangoUeditor.models import UEditorField
import os
import utils, oss2util

# 上传文件处理
@deconstructible
class AliyunStorage(Storage):
    def __init__(self, file_type =".jpg"):
        self.file_type = file_type
        #self.original_name = {}

    def save(self, relative_file_path, content, max_length=None):
        # save to content to disk
        save_path = os.path.join(settings.MEDIA_ROOT, 'upload', relative_file_path)
        utils.logger.debug('save path: %s', save_path)

        path = default_storage.save(save_path, ContentFile(content.read()))

        hash_code = oss2util.md5(path)
        target = hash_code + self.file_type
        # save original name
        utils.save_to_redis(target, relative_file_path)

        try:
            ret = oss2util.uploadFile(path, target)
            if ret and self.file_type == '.mp3':
                ffmpeg_utils.create_hls_files(path, hash_code)
        except Exception as e:
            utils.logger.error('save to aliyun fail: %s', str(e))
            raise Exception("save to aliyun oss fail")

        return target
    
    def exists(self, file_path):
        return OSS_exists(file_path)

    # we override this method to provide file's original name.
    # This is not a good prictise but is the only workaround to save the file name
    def path(self, name):
        try:
            return utils.get_from_redis(name)
        except Exception as e:
            return ""
    
    def url(self, name):
        if self.file_type == '.mp4':
            return vodutil.get_video_link(name)
        else:
            return oss2util.get_url(name)



class BaseImage(models.Model):
    name = models.CharField(max_length=50, blank=True, verbose_name=u'名称')
    img = models.ImageField(upload_to='', storage = AliyunStorage(), verbose_name=u'URL')
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)

    class Meta:
        abstract = True
    
    def __str__(self):
        if self.name is not None and len(self.name) != 0:
            #utils.logger.debug('In imagee str for %s', self.name)
            return self.name
        
        file_name = utils.get_from_redis(self.img.name)
        if file_name is not None:
            return file_name

        return self.img.name