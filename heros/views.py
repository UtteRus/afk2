from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import SpecificationsSerializer, SpecificationsHireSerializer
from .models import Specifications, Hero
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import permissions


class ViewHeroUserAPIList(APIView):
    #permission_classes = [permissions.IsAuthenticated]
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
        # heto = Hero.objects.get(pk=3)
        # us = heto.any_hero.all().values()
        # print(us)
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


class HireViewsAPI(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'hero/hire_views.html'

    def get(self, request):
        hire_hero = Specifications.objects.filter(hair=True)
        serializer = SpecificationsHireSerializer()
        return Response({'hire_hero': hire_hero, 'serializer': serializer})


class AddHireAPI(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'hero/add_hire.html'

    def get(self,request):
        serializer = SpecificationsHireSerializer()
        return Response({'serializer': serializer})

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
