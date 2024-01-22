from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import EmailField
from .models import field, login, Person, City


class RegisterForm(forms.ModelForm):
    class Meta:
        model = field
        fields = "__all__"


class LoginForm(forms.ModelForm):
    class Meta:
        model = login
        fields = "__all__"
Gender_Choice = [('Male', 'Male'),
                 ('Female', 'Female')]
MATERIAL_CHOICES = [('Debit Note Book', 'Debit Note Book'),
                    ('Pen', 'Pen'),
                    ('Exam Papers', 'Exam Papers'),
                    ('Pencil', 'Pencil'),
                    ('Eraser', 'Eraser')]

class PersonCreationForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=Gender_Choice, widget=forms.RadioSelect)
    Material = forms.MultipleChoiceField(label='MaterialRequired', choices=MATERIAL_CHOICES,
                                         widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Person
        fields = '__all__'
        labels = {'name': 'Full Name', 'email': 'Email Id', 'phoneNumber': 'Mobile Number', 'date': 'Date Of Birth',
                  'address': 'Address', 'country': 'Department', 'city': 'Sub Department'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()

        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.country.city_set.order_by('name')
