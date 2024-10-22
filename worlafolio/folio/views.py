from django.shortcuts import render, get_object_or_404
from folio.models import User, Projects

# Create your views here.
def index(request):
    user = User.objects.first()
    projects = Projects.objects.all()
    context = {
        "user": user,
        "projects": projects,
    }
    return render(request, "folio/index.html", context)
