from django.contrib import admin
from api.models import Card, Set, CardAndSetMap

admin.site.register(Set)
admin.site.register(Card)
admin.site.register(CardAndSetMap)
