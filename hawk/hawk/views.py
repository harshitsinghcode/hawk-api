from django.http import HttpResponse, JsonResponse

def hp(request):
    print("home page requested")
    friends=[
        'ankit',
        'ravi',
        'uttam'
    ]
    return JsonResponse(friends, safe=False )

