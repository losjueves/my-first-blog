#esto siempre
from django.shortcuts import render
#importar paquetes de funciones  que vallamos a usar
from django.utils import timezone
#importar los modelos que vamos a usar en las vistas
from .models import Post

# Create your views here.
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})