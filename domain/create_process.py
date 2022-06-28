from app.models import Process, User
from django.shortcuts import get_object_or_404
from domain.seed_serie import seed_serie

def create_process(n, k, user_id):
    
    user = get_object_or_404(User, pk=user_id)
    result = int(str(seed_serie(n, k))[0:4])

    process = Process.objects.create(user=user, n=n, k=k, result=result)
    process.save()

    return result