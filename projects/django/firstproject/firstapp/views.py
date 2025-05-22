from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from .forms import ReservationForm

# Create your views here.
def hello_world(request):
    return HttpResponse("Hello World!")


class HelloIndia(View):
    def get(self, request):
        return HttpResponse("Hello India!")


def home(request):
    form = ReservationForm()

    if request.method == 'POST':    # Send when user submits the form
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Reservation saved successfully!")
        else:
            return HttpResponse("Invalid data!")

    return render(request, 'index.html', {'form': form})