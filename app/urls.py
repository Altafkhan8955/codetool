from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app import views
from django.contrib.sitemaps.views import sitemap
from app.sitemaps import ModelSitemap
from django.views.generic import TemplateView

sitemaps = {
    'posts': ModelSitemap,
}

urlpatterns = [
   path('',views.index),
   path('clientreview/',views.ClientReview,name="clientreview"),
   path('contact/',views.Contact,name="contact"),
   path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
   path("robots.txt", TemplateView.as_view(template_name="robots.txt",content_type="text/plain")),
   #############################image tool######################################################################################### 
   path('remove_background_img/', views.process_image, name='background-remove'),
   path('image-resize', views.upload_and_resize, name='image-resize'),
   path('downloads/<int:pk>/', views.download_resized_image, name='download_resized_image'),
   path('resize/',  views.resizedimage, name='resize_image'),
   path('download/<int:pk>/', views.download_resize, name='download_resize'),
   path('convert_image_jpg_to_png/', views.uploadpng_image, name='uploadpng_image'),
   path('convertpng/<int:pk>/', views.convertpng_image, name='convertpng_image'),
   path('convert_image_format_to_jpg/', views.uploadjpg_image, name='uploadjpg_image'),
   path('download/<str:image_path>/', views.downloadjpg_image, name='downloadjpg_image'),
   path('convert_image_format_to_zip/', views.Convertzip_and_download, name='convertzip_and_download'),
   path('extract_zip_file', views.Extractzip, name='Extractzip'),
   path('extract-zip/', views.extract_zip, name='extract_zip'),
   path('downloadextractzip-image/<str:filename>/', views.downloadextractzip_image, name='downloadextractzip_image'),
   path('pdf_to_image/', views.pdf_to_image, name='pdf_to_image'),
   ############################pdf tool############################################################################################
   path('convert_image_to_pdf/', views.convert_image_to_pdf, name='convert_image_to_pdf'),
   path('combine_images_to_pdf/', views.combine_images_to_pdf, name='combine_images_to_pdf'),
   path('merge_two_pdf/', views.merge_pdfs_view, name='merge_pdfs'),
   path('text-to-pdf/', views.text_to_pdf, name='text_to_pdf'),
   path("excel_to_pdf",views.convert_excel_to_pdf, name="excel_to_pdf"),
   path('csv_to_pdf/', views.convert_csv_to_pdf, name='convert_csv_to_pdf'),
   path('word_to_pdf/', views.convert_word_to_pdf_and_download, name='convert_word_to_pdf'),
   path('ppt_to_pdf', views.convert_ppt, name='convert_ppt_to_pdf'),
   path('pdf_to_word/', views.pdf_to_word, name='pdf_to_word'),
   path('convert_pdf_to_ppt/', views.convert_pdf_to_ppt, name='convert_pdf_to_ppt'),
   path('convert_pdf_to_excel/', views.convert_pdf_to_excel, name='convert_pdf_to_excel'),
   path('pdf_to_csv', views.pdf_to_csv, name='pdf_to_csv'),
   path('downloadcsv/<str:file_name>/', views.download_csv, name='download_csv'),
   ###############################Other tool#############################################
   path('domain_info', views.get_domain_info, name='get_domain_info'),
   path('country_info/', views.get_country_info, name='get_country_info'),
   path('convert_video_to_audeo/', views.convert_video, name='convert_video'),
   path('download_audio/<str:audio_filename>/', views.download_audio, name='download_audio'),
   path('url_shortner', views.Shortener_url, name='url_shortner'),
   path('<str:short_url>/', views.redirect_original, name='redirect_original'),
   path('ip_lookup/', views.IpLookup, name='ip_lookup'),
   path('qr_generator/',views.Qr_Generator, name='qr_generator'),

]