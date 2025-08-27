from django import forms
from .models import Quote


class QuoteForm(forms.ModelForm):
    weight = forms.ChoiceField(
        choices=[(i, str(i)) for i in range(1, 11)],
    )
    class Meta:
        model = Quote
        fields = ['source', 'text','weight']

    def clean_source(self):
        source = self.cleaned_data['source']
        if Quote.objects.filter(source=source).count() >= 3:
            raise forms.ValidationError("Maximum 3 quotes for a single source permitted")
        return source
