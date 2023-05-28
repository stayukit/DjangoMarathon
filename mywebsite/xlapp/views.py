from django.shortcuts import render
from django.forms import CheckboxSelectMultiple, CheckboxInput, DateInput
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from .formsets import HotView

from .models import Movie

def index(request):
    return HttpResponseRedirect(reverse('update'))

class CreateMovieView(HotView):
    # Define model to be used by the view
    model = Movie
    # Define template
    template_name = 'xlapp/create.html'
    # Define custom characters/strings for checked/unchecked checkboxes
    checkbox_checked = 'yes' # default: true
    checkbox_unchecked = 'no' # default: false
    # Define prefix for the formset which is constructed from Handsontable spreadsheet on submission
    prefix = 'table'
    # Define success URL
    success_url = reverse_lazy('update')
    # Define fields to be included as columns into the Handsontable spreadsheet
    fields = (
        'id',
        'title',
        'director',
        'release_date',
        'parents_guide',
        'imdb_rating',
        'genre',
        'imdb_link',
    )
    # Define extra formset factory kwargs
    factory_kwargs = {
        'widgets': {
            'release_date': DateInput(attrs={'type': 'date'}),
            'genre': CheckboxSelectMultiple(),
            'parents_guide': CheckboxInput(),
        }
    }
    # Define Handsontable settings as defined in Handsontable docs
    hot_settings = {
        'contextMenu': 'true',
        'autoWrapRow': 'true',
        'rowHeaders': 'true',
        'contextMenu': 'true',
        'search': 'true',
        # When value is dictionary don't wrap it in quotes
        'headerTooltips': {
            'rows': 'false',
            'columns': 'true'
        },
        # When value is list don't wrap it in quotes
        'dropdownMenu': [
            'remove_col',
            '---------',
            'make_read_only',
            '---------',
            'alignment'
        ],
        'licenseKey': 'non-commercial-and-evaluation',
    }

class UpdateMovieView(CreateMovieView):
    template_name = 'xlapp/update.html'
    # Define 'update' action
    action = 'update'
    # Define 'update' button
    button_text = 'Update'

    hot_settings = {
        # 'columnSorting': 'true',
        'contextMenu': 'true',
        'autoWrapRow': 'true',
        'rowHeaders': 'true',
        'contextMenu': 'true',
        'search': 'true',
        'licenseKey': 'non-commercial-and-evaluation',
    }

