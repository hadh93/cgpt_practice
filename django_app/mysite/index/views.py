from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def waiting_view(request):
    if request.method == 'POST':
        # Send your API request here and get the response
        api_response = requests.get('your_api_url_here').json()
        return render(request, 'response.html', {'api_response': api_response})
    return render(request, 'waiting.html')

class ChatbotView(TemplateView):
    template_name = 'chatbot_ui.html'
