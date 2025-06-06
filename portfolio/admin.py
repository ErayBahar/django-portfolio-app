from django.contrib import admin
from .models import portfolioItem

@admin.register(portfolioItem)
class portfolioItemAdmin(admin.ModelAdmin):
    list_display = ('symbol','name_display','boughtPrice','currentPrice_display','amount','profit','worth_display')

    def worth_display(self,obj):
        return f"{obj.worth:.2f}"
    worth_display.short_description = "Total Worth"
    def currentPrice_display(self,obj):
        return f"{obj.currentPrice:.2f}"
    currentPrice_display.short_description = "Current Price"
    def name_display(self,obj):
        return obj.name
    name_display.short_description = "Name"


