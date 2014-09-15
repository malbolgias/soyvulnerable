from django.contrib import admin
from vulns.models import vulnerable

# Register your models here.

class vulnerableAdmin(admin.ModelAdmin):
  fieldsets = [
    (None,		{'fields' : ['vulnerable']}),
    ('Host', 		{'fields' : ('ip_add', 'hostname', 'port', 'city', 'country')}),
    ('Resultado',	{'fields' : ['result']}),
    ('Fecha',		{'fields' : ['date']}),
  ]
  list_display = ('ip_add', 'hostname', 'vulnerable', 'country', 'date')
  list_filter = ['vulnerable', 'country']
admin.site.register(vulnerable, vulnerableAdmin)