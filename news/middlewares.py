from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render


class TestMD(MiddlewareMixin):
    white_list = ['/login/', ]
    black_list = ['/black/', ]
    ret = {'status': 0, 'url': '', 'msg': ''}

    def process_request(self, request):
        # 通过该属性可以获取相对路径
        url = request.path_info
        if url in self.black_list:
            self.ret['msg'] = '非法操作'
            self.ret['url'] = '/news/login/'
        elif request.user:
            print(request.user.username)
            return None
        else:
            self.ret['msg'] = '请登录后重试'
            self.ret['url'] = '/news/login/'
        return render(request, 'jump.html', self.ret)
