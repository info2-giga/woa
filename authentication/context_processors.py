from django.contrib.auth import get_user_model
CustomUser = get_user_model()

def suggested_users_processor(request):
    # from ChatGPT
    if request.user.is_authenticated:
        suggested_users = CustomUser.objects.exclude(id=request.user.id).order_by('?')[:8]
    else:
        suggested_users = []
    return {'suggested_users': suggested_users}