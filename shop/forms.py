from django import forms


class PriceForm(forms.Form):
    min_price = forms.IntegerField(label="from", required=False)
    max_price = forms.IntegerField(label="to", required=False)
