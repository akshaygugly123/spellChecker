from django.shortcuts import render, HttpResponse
from django.shortcuts import get_object_or_404
from populateDBCode import scriptForExtractingData
from . import models


def lcs(X, Y):
    # find the length of the strings
    m = len(X)
    n = len(Y)

    # declaring the array for storing the dp values
    L = [[None] * (n + 1) for i in range(m + 1)]

    """Following steps build L[m + 1][n + 1] in bottom up fashion 
    Note: L[i][j] contains length of LCS of X[0..i-1] 
    and Y[0..j-1]"""
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

                # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m][n]
# end of function lcs

# Create your views here.
def delete_every_word(request):
    models.Word.objects.all().delete()
    return HttpResponse("all the words are deleted")


def index(request):
    return render(request, 'base.html')


def populateDB(request):
    list_of_words = scriptForExtractingData.applyBeautifulSoup()
    for word in list_of_words:
        wordObject = models.Word(word=word[0], partsOfSpeech=word[1], meaning=word[2])
        wordObject.save()

    return render(request, 'checkerApp/populate.html')


def search_result(request):
    word = str(request.POST.get('word')).capitalize()
    word_list = []
    for single_word in models.Word.objects.all():
        lcs_length = lcs(str(word).lower(),str(single_word.word).lower())
        if (abs(len(word) - lcs_length) == 0  and len(word) != len(single_word.word)) or (
                0 < abs(len(word) - lcs_length) < 3):
            word_list.append(single_word)
    try:
        word_object = models.Word.objects.get(word=word)
    except (KeyError, models.Word.DoesNotExist):
        data_for_frontend = {
            'word': None,
            'word_list': word_list,
        }
        return render(request, 'checkerApp/search_result.html', data_for_frontend)

    data_for_frontend = {
        'word': word_object,
        'word_list': word_list,
    }
    return render(request, 'checkerApp/search_result.html', data_for_frontend)
