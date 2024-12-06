from django import forms
from myapp.models import Appointment, ImageModel


class AppoitmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'

class ImageUpLoadForms(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = '__all__'