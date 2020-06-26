from django.core.mail import send_mail, EmailMessage

def sendmail(request):
	'''
	    send_mail(
	        'Subject',
	        'Email message',
	        'from@example.com',
	        ['to@example.com'],
	        fail_silently=False,
	    )
    '''
	nombre=request.user.name
	context={
		'news': 'correo para'+str(nombre)

	}
	template_name='emails/email.html'
	html_content=render_to_string(template_name, context)
	subject='correo prueba'+str(test)
	from_email='pricing@logisti-k.com.mx'
	to='vyruiz@logisti-k.com.mx'

	msg = EmailMessage(subject, html_content, from_email, [to])
	msg.content_subtype = "html"  # Main content is now text/html
	msg.send()

	return HttpResponse('Mail successfully sent')