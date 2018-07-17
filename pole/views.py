from django.shortcuts import render
from django.views import generic
from django.utils import timezone

from .models import User

class IndexView(generic.ListView):
	template_name = 'pole/index.html'
	context_object_name = 'user_list'

	def get_queryset(self):
		return User.objects.filter(creation_date__lte=timezone.now()).order_by('ranking')
