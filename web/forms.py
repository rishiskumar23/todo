from django import forms
from web.models import Todo


class TodoForm(forms.ModelForm):
    time = forms.TimeField(widget=forms.TimeInput(attrs={
                                                    'required': 'true',
                                                    'type': 'time'
                                                }))
    date = forms.DateField(widget=forms.DateInput(attrs={
                                                    'required': 'true',
                                                    'type': 'date'
                                                }))
    is_active = forms.BooleanField(widget=forms.HiddenInput(), initial=True)

    class Meta:
        model = Todo
        exclude = []
