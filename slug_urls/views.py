from rest_framework import generics, permissions
from rest_framework.views import APIView
from django.http import HttpResponseRedirect
from django.http import Http404
from django.db.models import F
from .permissions import *
from .serializers import *
from .models import *


class URLsListView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = URLsSerializerAuth

    def get_queryset(self):
        if self.request.user.is_staff:
            queryset = URLs.objects.all()
            return queryset
        queryset = URLs.objects.filter(author=self.request.user)
        return queryset

    # def get_serializer_class(self):
    #     if self.request.user.is_authenticated:
    #         self.serializer_class = URLsSerializerAuth
    #         return self.serializer_class
    #     self.serializer_class = URLsSerializer
    #     return self.serializer_class


class URLsDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = URLsSerializerAuth

    def get_queryset(self):
        if self.request.user.is_staff:
            queryset = URLs.objects.all()
            return queryset
        queryset = URLs.objects.filter(author=self.request.user)
        return queryset


class URLsCreateView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = URLs.objects.all()
    serializer_class = URLsSerializerAuth


class URLsShortView(APIView):
    def get(self, request, short_url):
        get_record = URLs.objects.filter(short_url=short_url)
        if get_record.first():
            get_record.update(views=F('views') + 1)
            return HttpResponseRedirect(redirect_to=get_record.first().orig_url)
        else:
            raise Http404
