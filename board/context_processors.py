from django.conf import settings
from django.contrib.sites.models import Site


def current_site(request):
    return {'current_site': Site.objects.get_current()}


def bugzilla_url(request):
    return {'bugzilla_url': settings.BUGZILLA_URL}
