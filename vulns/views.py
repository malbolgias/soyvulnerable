#coding: utf8 
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.utils import timezone
from vulns.models import vulnerable
from porc import Client
import nmap
import re
import lizepy
import orch

# Create your views here.
def index(request):
    #client_ip = request.META['REMOTE_ADDR']
    client = Client(orch.key)
    #Regex para detectar ips validas y evitar que se manipule la informacion recibida
    ValidIp = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$";
    client_ip = get_ip(request)
    check = False
    country = ""
    city = ""
    if (re.match(ValidIp, client_ip)):
      nm = nmap.PortScanner()
      #client_ip = "186.80.56.1/24"
      #Ejecutar nmap sobre puertos http y script de deteccion de vulnerabilidades
      nm.scan(client_ip, '80,8080,443,64680', arguments='--script=http-vuln-col -Pn -T5')
      #Iterar sobre los resultados del escaneo
      for host in nm.all_hosts():
        client_host = ('\nHost : %s (%s)' % (host, nm[host].hostname()))
        #Consultar datos de la ip frente a geoip
        geoip = lizepy.get_geoip(str(host))
        #Procesamiento de excepciones, en algunos casos geoip no devuelve los datos esperados
        try:
          if geoip.country_code:
            country = geoip.country_code
        except:
          country = ""
        try:
          if geoip.city:
            city = geoip.city
        except:
          city = ""
        for ports in nm[host].all_tcp():
            if nm[host]['tcp'][ports]['state'] == "open":
                if (re.search( 'Vulnerabilidad:.+', nm[host]['tcp'][ports]['script']['http-vuln-col'])):
                  vuln = vulnerable(ip_add=host, hostname=nm[host].hostname(), port=ports, date=timezone.now(), result = nm[host]['tcp'][ports]['script']['http-vuln-col'], country = country, city = city)
                  vuln.save()
                  output = nm[host]['tcp'][ports]['script']['http-vuln-col']
                  #Procesar texto recibido de nmap, para ser desplegado al usuario
                  check = re.search( 'Vulnerabilidad:.+', nm[host]['tcp'][ports]['script']['http-vuln-col'])
                  check = check.group()
                  #Parametro json para ser enviado, a orchestrate
                  vuln_json = { "ip": host, "hostname": nm[host].hostname(),  "port": ports, "data": nm[host]['tcp'][ports]['script']['http-vuln-col'], "Country": country, "City": city, "Vulnerable": True, "Date": str(timezone.now())}
                  response = client.post("vulnerables", vuln_json)
                  response.raise_for_status()
                else:
                  check = False
        if check == False:
          vuln = vulnerable(ip_add=host, hostname=nm[host].hostname(), port=ports, date=timezone.now(), result = "", vulnerable = False, country = country, city = city)
          vuln.save()
          #Parametro json para ser enviado, a orchestrate
          vuln_json = { "ip": host, "hostname": nm[host].hostname(),  "port": ports, "data": None, "Country": country, "City": city, "Vulnerable": False, "Date": str(timezone.now()) }
          response = client.post("vulnerables", vuln_json)
          response.raise_for_status()
      template = loader.get_template('vulns/index.html') 
      context = {'ip':client_ip, 'host':client_host, 'vulnerable':check}
      return render(request, 'vulns/index.html', context)
    else:
      context = {'ip':"Ip invalida", 'vulnerable':check}
      return render(request, 'vulns/index.html', context)
    
def home(request):
    context = { 'home':'Para probar su router haga click en el botón' }
    return render(request, 'vulns/home.html', context)
  
def problematica(request):    
    return render(request, 'vulns/problematica.html')
  
def contacto(request):    
    return render(request, 'vulns/contacto.html')
  
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
  
