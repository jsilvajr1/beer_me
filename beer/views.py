from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import BeerForm
from .models import Beer
from .serializers import BeerSerializer


def beer_list(request):
    beers = Beer.objects.all()
    serialized_beers = BeerSerializer(beers).all_beers
    return JsonResponse(data=serialized_beers, status=200)
    

def beer_detail(request, beer_id):
    beer = Beer.objects.get(id=beer_id)
    serialized_beer = BeerSerializer(beer).beer_detail
    return JsonResponse(data=serialized_beer, status=200)
    
@csrf_exempt
def new_beer(request):
    if request.method == "POST":
        form = BeerForm(request.POST)
        if form.is_valid():
            beer = form.save(commit=True)
            serialized_beer = BeerSerializer(beer).beer_detail
            return JsonResponse(data=serialized_beer, status=200)

@csrf_exempt
def edit_beer(request, beer_id):
    beer = Beer.objects.get(id=beer_id)
    if request.method == "POST":
        form = BeerForm(request.POST, instance=beer)
        if form.is_valid():
            beer = form.save(commit=True)
            serialized_beer = BeerSerializer(beer).beer_detail
            return JsonResponse(data=serialized_beer, status=200)


@csrf_exempt
def delete_beer(request, beer_id):
    if request.method == "POST":
        beer = Beer.objects.get(id=beer_id)
        beer.delete()
    return JsonResponse(data={'status': 'Successfully deleted beer.'}, status=200)