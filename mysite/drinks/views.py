from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_list_or_404
from django.http import HttpResponseBadRequest, response
from drinks.models import Drinks
from django.views.decorators.http import require_GET, require_http_methods 

@require_GET
def index_view(request):
    objects = Drinks.objects.select_related('brand').order_by('-likes')[:20]
    return render(request,template_name='drinks/index.html',context={"objects":objects})

@require_GET
def list_view(request):
    objects = get_list_or_404(Drinks.objects.select_related('brand').order_by('-likes')[:20])
    return render(request,template_name='drinks/list.html',context={"objects":objects})
