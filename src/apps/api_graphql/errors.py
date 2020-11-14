from graphene_django.views import GraphQLView
from django.utils.translation import LANGUAGE_SESSION_KEY, activate as select_language
class CustomGraphQLView(GraphQLView):
    @staticmethod
    def format_error(error):
        
        if hasattr(error, 'original_error') and error.original_error:
            formatted = {"message": str(error.original_error)}
            formatted['code'] = type(error.original_error).__name__.replace("Exception","")
            return formatted
        return GraphQLView.format_error(error)
    def dispatch(self, request, *args, **kwargs):
        self.__set_language_system(request)
        response = super().dispatch(request, *args, **kwargs)
        response = self.__set_language_cookie(request, response)
        return response

    def __set_language_cookie(self, request, response):
        if code := getattr(request, "set_language_cookie", None):
            response.set_cookie(LANGUAGE_SESSION_KEY, code)

        return response
    def __set_language_system(request,response):
        
        if LANGUAGE_SESSION_KEY in response.COOKIES:
            code = response.COOKIES[LANGUAGE_SESSION_KEY]
            select_language(code)

class InvalidIdException(Exception):
    pass