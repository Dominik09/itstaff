
from django.shortcuts import render_to_response
from loginsys.models import User

def main_page(request):
	args = {}
	if str(request.user) is not 'AnonymousUser':
		args['user'] = User.objects.get(username = request.user)
	return render_to_response('main.html', args)