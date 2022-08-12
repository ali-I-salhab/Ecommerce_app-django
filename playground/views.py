from django.shortcuts import render


def say_hello_fromstore(request):
    return render(request, 'hello.html', {'name': 'Mosh'})
