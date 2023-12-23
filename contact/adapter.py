from allauth.account.adapter import DefaultAccountAdapter


# Custom Account Adapter to modify default behavior
class CustomAccountAdapter(DefaultAccountAdapter):
    def get_login_redirect_url(self, request):
        return '/'

    def clean_email(self, email):
        return email.strip()
