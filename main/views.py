from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect   # Tambahkan import redirect di baris ini
from main.forms import BookForm
from main.models import Book
# Create your views here.
def show_main(request):
    books = Book.objects.all()

    context = {
        'name': 'Gistela Namasya Sinurat',
        'class': 'PBP A',
        'books': books
    }

    return render(request, "main.html", context)
def show_xml(request):
         data = Book.objects.all()
         return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
def create_book(request):
        form = BookForm(request.POST or None)

        if form.is_valid() and request.method == "POST":
            form.save()
            return redirect('main:show_main')

        context = {'form': form}
        return render(request, "create_book.html", context)
def show_json(request):
        data = Book.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
def show_xml_by_id(request, id):
        data = Book.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
def show_json_by_id(request, id):
        data = Book.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")