from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, Rater. You're at the movie ratings index.")
