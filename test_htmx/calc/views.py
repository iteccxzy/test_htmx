from django.shortcuts import render

# Create your views here.


def contact(request):
    if request.htmx:
        print(request.htmx.current_url)
        return render(request, 'partial_contact.html')
    return render(request, 'contact.html')

def edit(request):
    return render(request, 'edit.html')


