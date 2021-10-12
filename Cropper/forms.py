from PIL import Image
from django import forms
from django.core.files import File
# from .models import Photo

# class PhotoForm(forms.ModelForm):
#     x = forms.FloatField(widget=forms.HiddenInput())
#     y = forms.FloatField(widget=forms.HiddenInput())
#     width = forms.FloatField(widget=forms.HiddenInput())
#     height = forms.FloatField(widget=forms.HiddenInput())

#     class Meta:
#         model = Photo
#         fields = ('file', 'x', 'y', 'width', 'height',)

#     def save(self):
#         photo = super(PhotoForm, self).save()

#         x = self.cleaned_data.get('x')
#         y = self.cleaned_data.get('y')
#         w = self.cleaned_data.get('width')
#         h = self.cleaned_data.get('height')

#         image = Image.open(photo.file)
#         cropped_image = image.crop((x, y, w+x, h+y))
#         resized_image = cropped_image.resize((200, 200), Image.ANTIALIAS)
#         resized_image.save(photo.file.url)


#         return photo

# class ImageForm(forms.ModelForm):
#     class Meta:
#         model = Image
#         fields = '__all__'

CATEGORIES =( 
    ("1", "personal"), 
    ("2", "Facebook"), 
    ("3", "Snapchart"),   
    ("4", "Instargram"), 

)

class ImagesForm(forms.Form):
    image = forms.ImageField(required=True) 
    imagename = forms.CharField(required=True)
    description = forms.CharField(required=True)
    locaton = forms.CharField(required=True)
    category = forms.ChoiceField(choices=CATEGORIES, required=True)
