import graphene
from graphene_django import DjangoObjectType
from core.models import *


class AutherType(DjangoObjectType):
    class Meta:
        model = Auther
        fields = "__all__"


class NewsType(DjangoObjectType):
    class Meta:
        model = News
        fields = "__all__"


# simple e.g
class Query(graphene.ObjectType):
    # hello = graphene.String(default_value="Hi!")
    all_news = graphene.List(NewsType)
    all_authers = graphene.List(AutherType)

    def resolve_all_news(root, info):
        return News.objects.all()


schema = graphene.Schema(query=Query)
