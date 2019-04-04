from django.shortcuts import render,get_object_or_404,redirect
from django.http import JsonResponse
from .forms import ReviewForm


from rest_framework import viewsets          # add this
from .serializers import ReviewSerializer      # add this
from .models import Review
# Create your views here.
class ReviewView(viewsets.ModelViewSet):       # add this
      serializer_class = ReviewSerializer          # add this
      queryset = Review.objects.all() 


def ListView(request):
	queryset = Review.objects.all()
	data = {"result":''}
	if queryset:
		data = {"result":list(queryset.values('date','sku','rating','title', 'author', 'text','source'))}

	return JsonResponse(data)

def DetailView(request,pk):
	obj = get_object_or_404(Review,pk=pk)
	data = {

	'date':obj.date,
	'sku':obj.sku,
	'rating':obj.rating,
	'title':obj.title,
	'author':obj.author,
	'text':obj.text,
	'source':obj.source

	}
	return JsonResponse(data)

def CreateView(request):
	if request.method == 'POST':
		form = ReviewForm(request.POST)
		if form.is_valid():
			review = form.save(commit=False)
			review.save()

			return redirect('DetailView' , pk=review.pk)
	else:
		form = ReviewForm()

	return render(request, 'new_review.html', {'form': form})	


def UpdateView(request,pk):
	review = get_object_or_404(Review,pk=pk)
	form = ReviewForm(request.POST or None, instance=review)
	if form.is_valid():
		review = form.save(commit=False)
		review.save()

		return redirect('DetailView' , pk=review.pk)
		
	return render(request, 'new_review.html', {'form': form})

def DeleteView(request,pk):
	review = get_object_or_404(Review,pk=pk)
	review.delete()
	return redirect('ListView')









	

      