import django_filters as f

from .models import Stock, StockProduct


class StockModelFilter(f.FilterSet):
    
    stock = f.ModelChoiceFilter(
        queryset=Stock.objects.all(),
        field_name='stock'
    )
    
    class Meta:
        model = Stock
        fields = ['stock']