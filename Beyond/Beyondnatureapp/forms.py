from django import forms
from .models import enquire_now
# from captcha.fields import ReCaptchaField
# from captcha.widgets import ReCaptchaV2Checkbox



class SubmitForm(forms.Form):
    class Meta:
        model=enquire_now
        fields="__all__"
        # captcha= ReCaptchaField(Widget=ReCaptchaV2Checkbox)






# class LocationField(forms.CharField):
#     def __init__(self, *args, **kwargs):
#         super(LocationField, self).__init__(*args, **kwargs)
#         self.widget = forms.TextInput(attrs={'class': 'location-input'})