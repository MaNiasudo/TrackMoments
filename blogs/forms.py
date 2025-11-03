from django import forms


# make an form for our websites we want to get their urls

class IntegrationForm(forms.Form):
    type_choices = ("goodreads","goodreads"),("trakt","trakt")

    integration_type = forms.ChoiceField(choices=type_choices)
    integration_url = forms.URLField(max_length=200)