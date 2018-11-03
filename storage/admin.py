from datetime import timedelta, datetime

from django.contrib import admin

from storage.models import Product, Seller

DATE_FILTER_CHOICES = [
    (1, 'Last 24 hours'),
    (3, 'Last 3 days'),
    (7, 'Last 7 days')
]


class DateAddedFilter(admin.SimpleListFilter):
    title = 'date added'
    parameter_name = 'date_added'

    def lookups(self, request, model_admin):
        return DATE_FILTER_CHOICES

    def queryset(self, request, queryset):
        try:
            days = int(self.value())
        except TypeError:
            return queryset

        return queryset.filter(date_added__gte=datetime.now().date() - timedelta(days=days))


class DateUpdatedFilter(admin.SimpleListFilter):
    title = 'date updated'
    parameter_name = 'date_updated'

    def lookups(self, request, model_admin):
        return DATE_FILTER_CHOICES

    def queryset(self, request, queryset):
        try:
            days = int(self.value())
        except TypeError:
            return queryset

        return queryset.filter(date_updated__gte=datetime.now().date() - timedelta(days=days))


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_filter = [DateAddedFilter, DateUpdatedFilter]


admin.site.register(Seller)
