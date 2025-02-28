from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from django.views import View
from .models import Flight
from django import forms

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class RegisterFlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['name', 'flightType', 'price']


class RegisterFlightView(View):
    template_name = 'flights/register.html'

    def get(self, request):
        form = RegisterFlightForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = RegisterFlightForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['flightType'] == 'Select a flight type':
                form.add_error('flightType', 'Please select a valid flight type')
                return render(request, self.template_name, {'form': form})
            form.save()
            return redirect('home')
        else:
            return render(request, self.template_name, {'form': form})
        
class ListFlightsView(ListView):
    template_name = 'flights/list.html'
    model = Flight
    context_object_name = 'flights'
    # Order the flights
    queryset = Flight.objects.order_by('price')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class StatisticsView(View):
    template_name = 'flights/statistics.html'

    def get(self, request):
        flights = Flight.objects.all()
        national_flights = Flight.objects.filter(flightType='National').count()
        international_flights = Flight.objects.filter(flightType='International').count()
        national_prices = Flight.objects.filter(flightType='National').values_list('price', flat=True)
        national_prices = sum(national_prices) / len(national_prices)
        international_prices = Flight.objects.filter(flightType='International').values_list('price', flat=True)
        international_prices = sum(international_prices) / len(international_prices)
        return render(request, self.template_name, {'flights': flights, 'national_flights': national_flights, 'international_flights': international_flights, 'national_prices': national_prices, 'international_prices': international_prices})