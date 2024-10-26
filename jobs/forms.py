from django import forms
from .models import Job  # Import your Job model

class JobForm(forms.ModelForm):
    class Meta:
        model = Job  # Specify the model to use
        fields = ['title', 'description', 'company', 'location']  # Include your fields

    def __init__(self, *args, **kwargs):
        super(JobForm, self).__init__(*args, **kwargs)
        # Add CSS class to each field
        self.fields['title'].widget.attrs.update({'class': 'form-control'})  
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['company'].widget.attrs.update({'class': 'form-control'})
        self.fields['location'].widget.attrs.update({'class': 'form-control'})
