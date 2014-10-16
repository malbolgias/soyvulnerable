# Código fuente proyecto SoyVulnerable

Hace un poco más de un año descubrí una [vulnerabilidad](http://malbolgia.tumblr.com/post/63053321940/el-triste-estado-de-la-seguridad-en-el-servicio-de) sobre unos modelos de routers de la empresa Movistar, la vulnerabilidad se reportó ante colCERT (Grupo de Respuesta a Emergencias Cibernéticas de Colombia), pero su tramite duró mas de año y medio y no se realizó una solución efectiva. Durante este tiempo una empresa de seguridad rusa descubrió un ataque sistemático sobre estos dispositivos, en su estudio se descubrieron más de [300.000](http://www.inteco.es/technologyForecastingSearch/CERT/Alerta_Temprana/Bitacora_de_ciberseguridad/300M_routers_domesticos_comprometidos) dispositivos [vulnerados](http://www.team-cymru.com/ReadingRoom/Whitepapers/SOHOPharming.html), de estos 50.000 pertenecientes a Colombia.

Viendo la falta de gestión de las organizaciones responsables y los riesgos que corren las personas, decidí emprender la búsqueda de más fallas sobre estos dispositivos. Al momento de esta publicación, he detectado vulnerabilidades en al menos uno de los modelos de todos los grandes proveedores de internet del país. En la página se explican los riesgos, en el apartado de problemática. A futuro se agregarán posibles mitigaciones y guiones guía para el contacto con las empresas proveedoras de servicio.

Al entrar a la página pueden comprobar si el router que tienen en su hogar es vulnerable, también se puede probar desde dispositivos móviles, pero se debe estar conectado a la red Wifi.

https://soyvulnerable.com

## Aviso legal

El servicio soyvulnerable tiene dos fines; El primero es como servicio social y el segundo es de investigación académica. Para su funcionamiento la página recolecta datos de análisis de tráfico a través del servicio “Google analytics”.

En el momento que se pulsa el botón “Probar” se almacena en una base de datos y en [orchestrate](https://orchestrate.io/):

* IP
* Hostname
* País
* Ciudad
* Resultado

Aunque la información registrada no es información personal, si es delicada en específico, para los casos en que el resultado sea positivo. La información almacenada no sera compartida con ningún tercero con fines diferentes a los académicos.

En ningún momento se intentara explotar a las personas que accedan al servicio. Por seguridad propia no comparta capturas de pantalla donde se vea la dirección ip o el hostname probado. No me puedo hacer responsable por las actividades de terceros.

Las políticas de privacidad del servicio de Google las puede consultar [aquí](https://www.google.com/intl/es/policies/privacy/).