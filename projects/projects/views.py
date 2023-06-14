from django.http import JsonResponse


def landing(request):
    return JsonResponse({
        "status": "running",
    })

