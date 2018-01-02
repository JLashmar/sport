from sports.models import Sport, Sport_Category

def categories(request):
    all_categories = Sport_Category.objects.all()

    return {
        'categories': all_categories,
    }
