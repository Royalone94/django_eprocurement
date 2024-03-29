# yourapp/lookups.py
from ajax_select import register, LookupChannel
from .models import Product

@register('products')
class ProductsLookup(LookupChannel):

    model = Product

    def get_query(self, q, request):
        return self.model.objects.filter(name__icontains=q).order_by('name')[:50]

    def format_item_display(self, item):
        return u"<span class='tag'>%s</span>" % item.name