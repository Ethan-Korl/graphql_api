import graphene
from graphene_django import DjangoObjectType
from core.models import *


# simple e.g
class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")


schema = graphene.Schema(query=Query)
