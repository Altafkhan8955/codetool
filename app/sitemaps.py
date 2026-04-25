from django.contrib.sitemaps import Sitemap
from .models import SiteMaps

class ModelSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return SiteMaps.objects.all()

    def lastmod(self, obj):
        return obj.updated_at  # make sure this field exists

    def location(self, obj):
        return f"/127.0.0.1:8888/{obj.slug}/"