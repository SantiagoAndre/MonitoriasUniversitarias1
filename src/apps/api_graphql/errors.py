from graphene_django.views import GraphQLView



class CustomGraphQLView(GraphQLView):
    @staticmethod
    def format_error(error):
        
        if hasattr(error, 'original_error') and error.original_error:
            formatted = {"message": str(error.original_error)}
            formatted['code'] = type(error.original_error).__name__.replace("Exception","")
            return formatted
        return GraphQLView.format_error(error)



class InvalidIdException(Exception):
    pass