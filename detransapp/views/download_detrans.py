# coding: utf-8
import os
import mimetypes

from django.http import StreamingHttpResponse
from django.core.servers.basehttp import FileWrapper
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.conf import settings

'''class FileIterWrapper(object):
    def __init__(self, flo, chunk_size = 1024**2):
        self.flo = flo
        self.chunk_size = chunk_size

    def next(self):
        data = self.flo.read(self.chunk_size)
        if data:
            return data
        else:
            raise StopIteration

    def __iter__(self):
        return self'''


class DownloadDetransView(APIView):
    permission_classes = (IsAuthenticated, AllowAny)
    # @method_decorator(login_required)
    # @method_decorator(validar_imei())
    # @method_decorator(registro_log_sinc(0))
    @staticmethod
    def get():
        filename = 'detrans.sqlite.gz'
        db_path = "%s/%s" % (settings.MEDIA_ROOT, filename)

        response = StreamingHttpResponse(FileWrapper(open(db_path)), content_type=mimetypes.guess_type(db_path)[0])

        response['Content-Type'] = 'application/x-gzip'
        response['Content-Length'] = os.path.getsize(db_path)
        response['Content-Disposition'] = "attachment; filename=%s" % filename

        return response

        '''

        print 'dbfile.size : ',dbfile.size
        #return HttpResponse(FileIterWrapper(dbfile))
        response = HttpResponse(FileIterWrapper(dbfile))
        response['Content-Type'] = 'application/x-sqlite3'
        response['Content-Disposition'] = 'attachment; filename=%s' % "detrans.sqlite"
        #response['Content-Length'] = len(response.content)
        #response['Content-Length'] = os.path.getsize(db_path)'''

        return response


class DownloadDetransApkView(APIView):
    permission_classes = (IsAuthenticated, AllowAny)
    # @method_decorator(login_required)
    # @method_decorator(validar_imei())
    # @method_decorator(registro_log_sinc(0))
    def get(self, request):
        filename = 'app-detrans.apk'
        db_path = "%s/%s" % (settings.MEDIA_ROOT, filename)

        response = StreamingHttpResponse(FileWrapper(open(db_path)), content_type=mimetypes.guess_type(db_path)[0])

        response['Content-Type'] = 'application/vnd.android.package-archive'
        response['Content-Length'] = os.path.getsize(db_path)
        response['Content-Disposition'] = "attachment; filename=%s" % filename

        return response

        '''

        print 'dbfile.size : ',dbfile.size
        #return HttpResponse(FileIterWrapper(dbfile))
        response = HttpResponse(FileIterWrapper(dbfile))
        response['Content-Type'] = 'application/x-sqlite3'
        response['Content-Disposition'] = 'attachment; filename=%s' % "detrans.sqlite"
        #response['Content-Length'] = len(response.content)
        #response['Content-Length'] = os.path.getsize(db_path)'''

        return response
