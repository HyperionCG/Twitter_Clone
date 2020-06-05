from django.shortcuts import render

# Create your views here.

def notifications_view(request):
    user_data=request.user
    
    return render(request, 'index.html')