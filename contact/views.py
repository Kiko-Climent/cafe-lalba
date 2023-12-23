from django.shortcuts import render
from .forms import ContactForm


# View function for the contact form
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact/success_message.html')
    else:
        form = ContactForm()

    return render(request, 'contact/contact_form.html', {'form': form})
