from django import forms
from .models import ImageModel,ResizableImage,ConvertpngModel,ConvertjpgModel
from multiupload.fields import MultiFileField

#image background remove
class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['image']
#image resize size mb to kb
class ImageResizeForm(forms.Form):
    image = forms.ImageField()  
#image resize based height and width
class ResizeForm(forms.Form):
    height = forms.IntegerField()
    width = forms.IntegerField()
    image = forms.ImageField()
#convert image format jpg to png 
class ConvertpngForm(forms.ModelForm):
    class Meta:
        model = ConvertpngModel
        fields = ['image']
#convert image format jpg
class ConvertjpgForm(forms.ModelForm):
    class Meta:
        model = ConvertjpgModel
        fields = ['image']       
#convert image to zip format
class ConvertzipForm(forms.Form):
    images = MultiFileField(min_num=1, max_num=10, max_file_size=1024*1024*5, required=True)
#convert video to audio
class VideoForm(forms.Form):
    video_file = forms.FileField()
#Keyword Density checker
class KeywordForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 6, 'class': 'form-control'}),
        label="Enter Text"
    )
    keyword = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="Enter Keyword"
    )
#page speed checker
class URLForm(forms.Form):
    url = forms.URLField(
        label="Enter Website URL",
        widget=forms.URLInput(attrs={'class': 'form-control'})
    )



