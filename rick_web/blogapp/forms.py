from django import forms



# Contact Page Form
#
class ContactForm(forms.Form):
    name  = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    msg   = forms.CharField(required=True, widget=forms.Textarea)

