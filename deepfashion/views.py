from django.http import HttpResponse


def index(request):
    msg = "deepfashion"
    return HttpResponse(msg, content_type='text/plain')
