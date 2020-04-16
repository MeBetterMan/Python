from django.utils.deprecation import MiddlewareMixin


class MyMiddle(MiddlewareMixin):
    def process_request(self,req):
        print('get参数为：%s'% req.GET.get('a') )
