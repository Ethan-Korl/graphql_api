from graphene_django.views import GraphQLView
from django.contrib import admin
from django.urls import path
from core.schema import schema

urlpatterns = [
    # path("graphql/", GraphQLView.as_view(graphiql=True, schema=schema)),
    path("", GraphQLView.as_view(graphiql=True, schema=schema)),
]
