from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .forms import EditSpecificationsHeroForm
from .models import Specifications, Hero


def view_hero_user(request):
    name = 'admin'
    my_hero = Specifications.objects.filter(user=3)
    return render(request, 'hero/view_hero_user.html', {"my_hero": my_hero})


def edit_hero(request, specifications_id):
    post = get_object_or_404(Specifications, pk=specifications_id)
    heros_spec = Specifications.objects.get(pk=specifications_id)
    my_initial = {'named_item': heros_spec.named_item,
                  'furniture': heros_spec.furniture,
                  'engraving': heros_spec.engraving,
                  'evolution': heros_spec.evolution,
                  'hair': heros_spec.hair,
                  'hero': heros_spec.hero,
                  'user': heros_spec.user, }
    if request.method == 'POST':
        form = EditSpecificationsHeroForm(request.POST, instance=heros_spec)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('view_hero_user')
    else:
        form = EditSpecificationsHeroForm(initial=my_initial)

    my_dict = {
        'pk': specifications_id,
        'user_name': f'{heros_spec.user.username} {heros_spec.hero.hero_name}',
        'form': form
    }
    return render(request, 'hero/edit_hero_user.html',
                  context=my_dict)
