from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap
from django.views.i18n import JavaScriptCatalog
from blog.api.views import CustomCommentCreate
from djangocaptchav2.decorators import check_recaptcha


sitemaps = {
    "posts": PostSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('comments/api/comment/', check_recaptcha(CustomCommentCreate().as_view()), name='comments-xtd-api-create'),
    path('comments/', include('django_comments_xtd.urls')),
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    path('', include('blog.urls')),
    path('summernote/', include('django_summernote.urls')),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
    #path('',views.index, name="homepage"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT)
