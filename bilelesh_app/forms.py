from django import forms

class BookForm(forms.Form):
    start_date = forms.DateTimeField
    end_date = forms.DateTimeField
    room_type = forms.CharField
    people_count = forms.IntegerField
    phone_number = forms.IntegerField