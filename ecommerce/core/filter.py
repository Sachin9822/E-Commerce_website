from django_filters import *
from .models import *

class ItemFilter(FilterSet):
    title = CharFilter(field_name='title',lookup_expr="icontains")
    class Meta:
        model = Items
        fields = ['title','category','label']
