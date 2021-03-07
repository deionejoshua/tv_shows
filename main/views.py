from django.shortcuts import render, redirect
from .models import Shows
from django.contrib import messages

def index(request):
    return redirect('/shows')

def shows(request):
    context = {
        "all_shows" : Shows.objects.all()
    }
    return render(request, 'shows.html', context)


def new(request):
    return render(request, 'create_shows.html')


def create_show(request):
    errors = Shows.objects.validater(request.POST)
    if len(errors) > 0:
        for msg in errors.values():
            messages.error(request, msg)
        return redirect('/shows/new')

    show_created = Shows.objects.create(
        show_title = request.POST['show_title'],
        show_network = request.POST['show_network'],
        show_release_date = request.POST['show_release_date'],
        show_description = request.POST['show_description']
    )

    return redirect(f'shows/{show_created.id}')


def display_show(request, Shows_id):
    context = {
        "show" : Shows.objects.get(id = Shows_id)
        }
    return render(request, 'show_details.html', context)


def edit_shows(request, Shows_id):
    context = {
        "current_show" : Shows.objects.get(id = Shows_id )
        }
    return render(request, 'edit.html', context)


def update_show(request, Shows_id):
    errors = Shows.objects.validater(request.POST)
    if len(errors) > 0:
        for msg in errors.values():
            messages.error(request, msg)

        return redirect(f'/shows/{Shows_id}/edit')
    update_show = Shows.objects.get(id = Shows_id)
    update_show.show_title = request.POST['show_title']
    update_show.show_network = request.POST['show_network']
    update_show.show_release_date = request.POST['show_release_date']
    update_show.show_description = request.POST['show_description']
    update_show.save()
    return redirect(f'/shows/{Shows_id}')


def delete(request, Shows_id):
    delete_show = Shows.objects.get(id = Shows_id)
    delete_show.delete()
    return redirect('/shows')