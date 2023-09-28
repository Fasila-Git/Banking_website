from .models import AllDist,AllBranch


def dist_links(request):
    links = AllDist.objects.all()
    return dict(link=links)

# def branch_link(request):
#     branch=AllBranch.objects.all()
#     return dict(branch=branch)