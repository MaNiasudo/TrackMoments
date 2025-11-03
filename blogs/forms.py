from django import forms
from .models import Integration


# make an form for our websites we want to get their urls
# We use modelform if we want to pass it into our createview and use this form
#We need to have meta class and specify what model so createview can undrstandd what we looking for
class IntegrationForm(forms.ModelForm):
     class Meta:
        model = Integration
        fields = ['integration_type', 'integration_url']

