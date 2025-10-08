from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # Добавим AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    """
    Пользовательская форма для регистрации нового пользователя.
    """
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Применяем Bootstrap класс 'form-control' ко всем виджетам
        for field_name, field in self.fields.items():
            if isinstance(field.widget, (forms.TextInput, forms.EmailInput, forms.PasswordInput)):
                field.widget.attrs.update({'class': 'form-control'})

# --- НОВАЯ ЧАСТЬ: Создадим форму для входа, чтобы применить стили Bootstrap ---
class CustomAuthenticationForm(AuthenticationForm):
    """
    Пользовательская форма для входа.
    Применяет стили Bootstrap к полям.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, (forms.TextInput, forms.PasswordInput)):
                field.widget.attrs.update({'class': 'form-control'})
