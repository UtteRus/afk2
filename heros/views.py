from django.forms import model_to_dict
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import SpecificationsSerializer
from .forms import EditSpecificationsHeroForm
from .models import Specifications, Hero
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer


class ViewHeroUserAPIList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'hero/view_hero_user.html'

    def get(self, request):
        my_hero = Specifications.objects.filter(user=3)
        return Response({'my_hero': my_hero})


class EditHeroAPI(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'hero/edit_hero_user.html'

    def get(self, request, specifications_pk):
        heros_spec = get_object_or_404(Specifications, pk=specifications_pk)
        serializer = SpecificationsSerializer(heros_spec)
        return Response({'serializer': serializer,
                         'heros_spec': heros_spec})

    def post(self, request, specifications_pk):
        heros_spec = get_object_or_404(Specifications, pk=specifications_pk)
        serializer = SpecificationsSerializer(heros_spec, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer,
                             'heros_spec': heros_spec})
        serializer.save()
        return redirect('view_hero_user')

# def edit_hero(request, specifications_id):
#     post = get_object_or_404(Specifications, pk=specifications_id)
#     heros_spec = Specifications.objects.get(pk=specifications_id)
#     # heros_spec = Specifications.objects.values().get(pk=specifications_id)
#     my_initial = {'named_item': heros_spec.named_item,
#                   'furniture': heros_spec.furniture,
#                   'engraving': heros_spec.engraving,
#                   'evolution': heros_spec.evolution,
#                   'hair': heros_spec.hair,
#                   'hero': heros_spec.hero,
#                   'user': heros_spec.user, }
#     if request.method == 'POST':
#         form = EditSpecificationsHeroForm(request.POST, instance=heros_spec)
#         if form.is_valid():
#             form.save()
#             return redirect('view_hero_user')
#     else:
#         form = EditSpecificationsHeroForm(initial=my_initial)
#
#     my_dict = {
#         'pk': specifications_id,
#         'user_name': f'{heros_spec.user.username} {heros_spec.hero.hero_name}',
#         'form': form
#     }
#     return render(request, 'hero/edit_hero_user.html',
#                   context=my_dict)
