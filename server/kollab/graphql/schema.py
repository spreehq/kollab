import graphene

from catalogue.models import BrandAssociations, Brand
from graphene_django.types import DjangoObjectType


class BrandType(DjangoObjectType):
    class Meta:
        model = Brand


class Query(graphene.ObjectType):
    search = graphene.List(BrandType, brand=graphene.String())

    def resolve_search(self, info, **kwargs):
        try:
            b = Brand.objects.get(name__iexact=kwargs.get('brand').lower())
            return Brand.objects.filter(id__in=BrandAssociations.objects.filter(source=b).values_list('destination'))
        except Brand.DoesNotExist:
            return None
        except BrandAssociations.DoesNotExist:
            return None

        return None
