from django.shortcuts import render
from django.http import HttpResponse


# contact edit
def contact(request):
    if request.htmx:
        print(request.htmx.current_url)
        return render(request, 'partial_contact.html')
    return render(request, 'contact.html')

def edit(request):
    return render(request, 'edit.html')

# load row
def load(request):
    if request.htmx:
        return render(request, 'load_2.html')
    return render(request, 'load.html')


# delete row
def delete_row(request):
    if request.htmx:
        return HttpResponse("")
    return render(request, 'delete-row.html')

def lazy(request):
    if request.htmx:
        return render(request, 'lazy2.html')
    return render(request, 'lazy-loading.html')

def search(request):
    return render(request, 'search.html')