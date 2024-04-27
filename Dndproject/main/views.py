from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    if request.method == 'POST':
        input_text = request.POST.get('inputText', '')
        print(input_text)
        return HttpResponse(f'Введенный текст: {input_text}')
    else:
        return render(request, 'index.html')