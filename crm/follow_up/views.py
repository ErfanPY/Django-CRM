from django.contrib.auth.decorators import login_required

from django.shortcuts import render

from follow_up.forms import FollowUpsForm


@login_required
def create_follow_ups_view(request):
    """
        Return a html contains follow up creation form 
    """

    form_instance = FollowUpsForm()

    return render(request, 'follow_ups/follow_ups_form.html',
        {
            'form': form_instance,
            'page_title': 'Create a follow up',
            'form_method': 'POST',
            'form_action': '/follow_up/api/',
            'success_message': 'successfuly created follow ups.',
        }
    )


@login_required
def list_follow_ups_view(request):
    """
        Returns a html with a empty table to filled by ajax.
    """

    return render(request, 'follow_ups/follow_ups_list.html',
        {
            'page_title': 'follow ups list'
        }
    )
