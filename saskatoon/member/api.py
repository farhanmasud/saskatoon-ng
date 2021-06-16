
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from .models import Person
from harvest.models import Property
from .forms import PersonForm

class PersonCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Person
    form_class = PersonForm
    template_name = 'app/generic/model_form.html'
    success_message = "New Person registered successfully!"

    def get(self, request, *args, **kwargs):
        try:
            # registering new owner based on pending property
            p = Property.objects.get(id=request.GET['pid'])
            initial = { 'first_name': p.pending_contact_name,
                        'phone': p.pending_contact_phone.replace(" ", "-"),
                        'email': p.pending_contact_email,
                        'street_number': p.street_number,
                        'street': p.street,
                        'complement': p.complement,
                        'postal_code': p.postal_code,
                        'neighborhood': p.neighborhood,
                        'city': p.city,
                        'state': p.state,
                        'country': p.country,
                        'newsletter_subscription': p.pending_newsletter,
                        'comments': p.additional_info,
                        'pending_property_id': p.id
            }
        except KeyError:
            initial = None

        title = "Person Registration"
        context = {'form': PersonForm(initial=initial), 'title': title}

        return render(request, 'app/generic/model_form.html', context)

    def get_success_url(self):
        try:
            property_id = self.request.GET['pid']
            return reverse_lazy('property-detail', kwargs={'pk': property_id})
        except KeyError:
            return reverse_lazy('home')
