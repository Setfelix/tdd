from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item
# Create your views here.

def home_page(request):

    # item = Item()
    # item.text = request.POST.get('item_text', '')
    # item.save()

    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')

    #     new_item_text = request.POST['item_text']
    #     Item.objects.create(text=new_item_text)
    # else:
    #     new_item_text = ''

    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
    # return render(request, 'home.html', {
    #     'new_item_text': new_item_text,
    #     })
    # return HttpResponse(request.POST['item_text'])
    # return render(request, 'home.html')

