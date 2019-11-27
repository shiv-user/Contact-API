from django.shortcuts import render
from rest_framework import generics
from django.db.models import Q
from .models import contact
from .serializers import ContactSerializer
from django.views.generic import TemplateView, ListView


class ContactList(generics.ListCreateAPIView):
	queryset = contact.objects.all()
	serializer_class = ContactSerializer

class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = contact.objects.all()
	serializer_class = ContactSerializer


class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = contact
    template_name = 'search.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = contact.objects.filter(
            Q(name__icontains=query) | Q(number__icontains=query)
        )
        return object_list
