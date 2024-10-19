from django.shortcuts import render, get_object_or_404
from folio.models import User

# Create your views here.
def index(request):
    user = User.objects.first()
    context = {
        "user": user,
    }
    return render(request, "folio/index.html", context)
