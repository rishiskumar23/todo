from django.contrib.sites.models import Site


def get_site_url_without_scheme():
    domain = Site.objects.get_current().domain
    if domain.endswith('/'):
        return domain[:-1]
    else:
        return domain
