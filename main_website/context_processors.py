from cubs.models import Post as CubPosts
from scouts.models import Post as ScoutPosts
from beavers.models import Post as BeaverPosts

def posts(request):
    return {
        'beavers_all_posts': BeaverPosts.objects.order_by('date_posted'),
    }

def posts(request):
    return {
        'cubs_all_posts': CubPosts.objects.order_by('date_posted'),
    }

def posts(request):
    return {
        'scouts_all_posts': ScoutPosts.objects.order_by('date_posted'),
    }