# Create your views here.
from django.contrib.auth.models import User, Group
from django.http import Http404

from rest_framework import viewsets
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status

from api.models import Set, Card, CardAndSetMap
from api.serializers import SetSerializer


class SetView(views.APIView):
    def get(self, request, pk, format=None):
        set = Set.objects.get(pk=pk)
        cards = Card.objects.filter(cardandsetmap__set_id_id__exact=pk)
        set_with_card = SetDetail(set, cards)
        return Response(SetSerializer(set_with_card).data)


class SetDetail(object):
    def __init__(self, set, cards):
        self.set_id=set.set_id
        self.pub_date = set.pub_date
        self.cards = cards



