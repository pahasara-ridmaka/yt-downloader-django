from typing import Any, Mapping
from django import forms
from django.forms.renderers import BaseRenderer
from django.forms.utils import ErrorList
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit

resolutions = (
        ('720p', '720p'),
        ('480p', '480p'),
        ('360p', '360p'),
    )

url_tailwindcss_class = "outline-none w-1/3 h-12 bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block p-2.5 dark:placeholder-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500"

res_tailwindcss_class = " shadow-sm hover:shadow-md outline-none h-12 rounded-md border border-purple-700 text-sm px-5 font-semibold text-white bg-violet-500"

class MyForm(forms.Form):
    url = forms.CharField(max_length=150,label="",widget=forms.TextInput(attrs={"class":url_tailwindcss_class, 'placeholder':"https://www.youtube.com/watch?v=uJp4PaDkux0"}))
    res = forms.ChoiceField( choices=resolutions, required=True, label="Choose Resolution: ", widget=forms.Select(attrs={"class":res_tailwindcss_class}))

    # def __init__(self, *args, **kwargs):
    #     super(MyForm, self).__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_method = 'post'
    #     self.helper.layout = Layout(
    #         Field('url', css_class='block w-1/5 p-2 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'),
    #         Field('res', css_class='custom-select-container')
    #     )

    
    
   

