from django.shortcuts import redirect, render
from pydictionary import Dictionary
# Create your views here.
def home(request):
    return render(request, 'index.html')

def search(request):
    search = request.GET.get('search')
    if search:
        dict = Dictionary(search)
        meaning = dict.meanings()
        synonyms = dict.synonyms()
        antonyms = dict.antonyms()

        context = {
            'search':search,
            'meaning':meaning[0],
            'synonyms':synonyms,
            'antonyms':antonyms,
        }
        # print(search)
        # print(meaning)
        return render(request, 'index.html', context)
    else:
        return redirect('/')