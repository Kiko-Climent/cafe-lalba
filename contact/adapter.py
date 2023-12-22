from allauth.account.adapter import DefaultAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):
    def get_login_redirect_url(self, request):
        return '/'

    def clean_email(self, email):
        return email.strip()
