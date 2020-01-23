from rest_framework.renderers import JSONRenderer


class BaseResponse(object):
    """
    封装的返回信息类
    """

    def __init__(self):
        self.code = 1000
        self.data = None
        self.error = None

    @property
    def dict(self):
        return self.__dict__


class YgJSONRenderer(JSONRenderer):
    """
    自行封装的渲染器
    """

    def render(self, data, accepted_media_type=None, renderer_context=None):
        """
        如果使用这个render，
        普通的response将会被包装成：
            {"code":200,"data":"X","error":"X"}
        这样的结果
        使用方法：
            - 全局
                REST_FRAMEWORK = {
                'DEFAULT_RENDERER_CLASSES': ('utils.yg_response.YgJSONRenderer', ),
                }
            - 局部
                class UserCountView(APIView):
                    renderer_classes = [YgJSONRenderer]

        :param data: {"detail":"X"}
        :param accepted_media_type:
        :param renderer_context:
        :return: {"code":200,"data":"X","error":"X"}
        """
        response_body = BaseResponse()
        response_body.code = renderer_context.get("response").status_code

        if response_body.code >= 400:
            response_body.error = data.get("detail", {"detail": "没有具体的提示信息"})
        else:
            response_body.data = data

        return super(YgJSONRenderer, self).render(response_body.dict, accepted_media_type, renderer_context)
