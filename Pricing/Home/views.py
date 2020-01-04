from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.urls import reverse
from django.contrib.auth.decorators import login_required
@login_required

def Home(request):
	if (request.user.is_authenticated):
		return render(request,'Home.html')
	else:
		return HttpResponseRedirect('/')

def redireccionar(request):
	if (request.user.is_authenticated):
		return HttpResponseRedirect('Home')
	else:
		return HttpResponseRedirect('/accounts/login')


def TestJson(request):
	return render(request, 'TestJson.html')

@login_required
def sendmail(request,test):
	'''
	    send_mail(
	        'Subject',
	        'Email message',
	        'from@example.com',
	        ['to@example.com'],
	        fail_silently=False,
	    )
    '''
	context={
		'news': 'We have good news!'+str(test)

	}
	template_name='emails/email.html'
	html_content=render_to_string(template_name, context)
	subject='subject'
	from_email='from@example.com'
	to='vyruiz@logisti-k.com.mx'

	msg = EmailMessage(subject, html_content, from_email, [to])
	msg.content_subtype = "html"  # Main content is now text/html
	msg.send()

	return HttpResponse('Mail successfully sent')

def testredirect(request):
	test='11'
	return redirect('Home:sendmail',test=test)

def TESTMETRONIC(request):
	return render(request,'testmetronic.html')