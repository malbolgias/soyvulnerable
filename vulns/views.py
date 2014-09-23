#coding: utf8 
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.utils import timezone
from vulns.models import vulnerable
import nmap
import re
import lizepy

# Create your views here.
def index(request):
    #client_ip = request.META['REMOTE_ADDR']
    ValidIp = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$";
    client_ip = get_ip(request)
    check = False
    country = ""
    city = ""
    if (re.match(ValidIp, client_ip)):
      nm = nmap.PortScanner()
      #client_ip = "186.80.56.1/24"
      nm.scan(client_ip, '80,8080,443,64680', arguments='--script=http-vuln-une -Pn')
      for host in nm.all_hosts():
	client_host = ('\nHost : %s (%s)' % (host, nm[host].hostname()))
	geoip = lizepy.get_geoip(str(host))
	if geoip.country_code:
	  country = geoip.country_code
	if geoip.city:
	  city = geoip.city
	for ports in nm[host].all_tcp():
	    if nm[host]['tcp'][ports]['state'] == "open":
		if (re.search( 'Vulnerabilidad:.+', nm[host]['tcp'][ports]['script']['http-vuln-une'])):
		  vuln = vulnerable(ip_add=host, hostname=nm[host].hostname(), port=ports, date=timezone.now(), result = nm[host]['tcp'][ports]['script']['http-vuln-une'], country = country, city = city)
		  vuln.save()
		  output = nm[host]['tcp'][ports]['script']['http-vuln-une']
		  check = re.search( 'Vulnerabilidad:.+', nm[host]['tcp'][ports]['script']['http-vuln-une'])
		  check = check.group()
		else:
		  check = False
	if check == False:
	  vuln = vulnerable(ip_add=host, hostname=nm[host].hostname(), port=ports, date=timezone.now(), result = "", vulnerable = False, country = country, city = city)
	  vuln.save()
      template = loader.get_template('vulns/index.html')
      context = {'ip':client_ip, 'host':client_host, 'vulnerable':check}
      return render(request, 'vulns/index.html', context)
    else:
      context = {'ip':"Ip invalida", 'vulnerable':check}
      return render(request, 'vulns/index.html', context)
    
def test(request, ip):
    return HttpResponse("You're looking at ip %s" % ip)
  
def home(request):
    context = { 'home':'Para probar su router haga click en el botón' }
    return render(request, 'vulns/home.html', context)
  
def problematica(request):    
    return render(request, 'vulns/problematica.html')
  
def get_ip(request):
    try:
      x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
      if x_forward:
	ip = x_forward.split(",")[0]
      else:
	ip = request.META.get("REMOTE_ADDR")
    except:
      ip = ""
    return ip
  
