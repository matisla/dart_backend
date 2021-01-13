from django import forms


class ScoreForm(forms.Form):
    score = forms.IntegerField(label="score", required=False)
