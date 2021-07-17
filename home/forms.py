from django import forms

NUMS = [
    ('past', 'past'),
    ('future', 'future'),


]


class CHOICES(forms.Form):
    NUMS = forms.CharField(widget=forms.RadioSelect(choices=NUMS))
