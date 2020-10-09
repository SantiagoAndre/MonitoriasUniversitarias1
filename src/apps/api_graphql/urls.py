from django.urls import path
from .errors import CustomGraphQLView as GraphQLView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [

    path('', csrf_exempt(GraphQLView.as_view(graphiql=True))),

]