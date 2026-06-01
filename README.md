# *Integrantes*
## **Keiner Sebastián Rios** ,  **Nickolas Sarmiento Rojas** & **Maria Camila Osorio Tuberquia**
# *Vínculos académicos y descripción*
### Keiner & Nickolas, ambos son estudiantes de la Universidad de Antioquia pertenecientes al cuarto semestre del programa Ingenieria Industrial  
> Keiner cuyas habilidades resaltan en la redacción técnica de contenidos, atención al cliente y marketing digital sumado a sus fortalezas que son el liderazgo, pensamiento critico y gestion del tiempo haran una trio imparable que nos servira para impulsar este software.
> Camila cuyas habilidades resaltan su disciplina y compromiso, con una mentalidad de crecimiento que se crece ante los retos. Además, tu compañerismo te convierte en un pilar valioso para cualquier equipo.
> Nickolas cuyas habilidades en administración de sistemas, gestión de proyectos e interpretacion nos dara un plus para desarrollar este software acompañado de sus fortalezas como la adaptabilidad, toma de decisiones y su iniciativa.
# *Loans_Nicker*
¿Prestaste tus herramientas, un juego o ese electrodoméstico y no recuerdas a quién? Con Loans_Nicker, el caos se termina, somos la herramienta definitiva que te ayudara para gestionar tus activos y nuestro fuerte la OGR: organizamos, gestionamos y recuperamos; con su implementacion llevaremos tu programa al maximo Porque lo que se presta, se cuida, y porque el control no debe ser un estres.

![imagen del proyecto](https://raw.githubusercontent.com/sebastiankrios/Loans_Nicker/refs/heads/main/img/Gemini_Generated_Image_l0eqk6l0eqk6l0eq.png)
# Licencia

<a href="https://github.com/sebastiankrios/Loans_Nicker">Loans_Nicker</a> © 2026 by <a href="https://github.com/sebastiankrios">Sebastian Rios</a> is licensed under <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">CC BY-NC-SA 4.0</a><img src="https://mirrors.creativecommons.org/presskit/icons/cc.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/by.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/nc.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/sa.svg" alt="" style="max-width: 1em;max-height:1em;margin-left: .2em;">
# *Visión*
Nuestro software actúa como un asistente logístico digital que permite a los usuarios registrar, rastrear y recuperar sus pertenencias como videojuegos, herramientas, electrodomésticos, etc. de manera eficiente y profesional lo que hace diferente a Loans_Nicker de los demas porque este formaliza el proceso de préstamo mediante un sistema de inventario inteligente y un motor de notificaciones proactivas
### Objetivos
> Crear un programa de consola visualmente amigable al usuario, en donde permita gestionar el préstamo de artículos, gestionando mediante archivos planos la información, para posteriormente exportar los resultados a un CSV usando Python.

> Desarrollar un sistema de validación de datos y lógica difusa en Python que garantice la integridad de la información del inventario (videojuegos, libros, herramientas, etc.) y automatice la generación de facturas de venta con recargos legales ante el incumplimiento de los plazos de devolución.

> Implementar un ciclo de desarrollo basado en metodologías ágiles y control de versiones mediante GitHub, documentando requisitos funcionales, planes de proyecto y manuales de usuario para asegurar la escalabilidad y sostenibilidad del gestor de préstamos.
### Beneficios
>Ahorro de Tiempo, historial de Confianza, control Total, preservación de Activos
# *Requisitos*
### Requisitos funcionales
#### Gestión de Usuarios:
> El sistema debe registrar nombre, apellido, documento y correo con validaciones específicas (nombres sin números, documento numérico de 3-15 dígitos y correo con formato
#### Tiempos de Préstamo:
> Al crear un usuario, se debe definir un plazo fijo de préstamo entre 5, 10, 15 o 30 días.
#### Registro de Ítems:
> Cada objeto debe tener nombre ($\ge 3$ letras), categoría (Videojuegos, Libros, Herramientas, etc.), precio de compra e ID alfanumérico único.
#### Valoración por Lógica Difusa:
> El programa debe permitir registrar el estado de calidad del ítem usando lógica difusa al momento del ingreso.
#### Control de Préstamos y Devoluciones:
> Solo se permite prestar a usuarios registrados; las devoluciones deben generar un certificado en texto plano (.txt) con el ID y fecha.
#### Generación de Ventas:
> Los ítems con más de 30 días de préstamo deben facturarse automáticamente al prestador, sumando un "impuesto por conchudez" del 23% sobre el precio de compra.
#### Módulo Administrativo:
> Acceso restringido con usuario y contraseña para consultar estadísticas (total de ventas, pagos, lista de usuarios y récords de préstamos).
### Requisitos no funcionales
#### Interfaz:
> El software debe contar con un menú amigable basado en consola.
#### Lenguaje de Programación:
> Todo el desarrollo debe ser realizado en Python.
#### Persistencia de Datos:
> El almacenamiento se hará mediante archivos planos, con capacidad de exportar resultados a formato CSV.
#### Estructura de Código:
> El proyecto debe organizar el código en una carpeta llamada src y la documentación en doc dentro del repositorio

# *Plan de Proyecto*
## Actividades
> Para el desarrollo de Loans_Nicker, se seguirá un modelo de desarrollo ágil donde el docente actúa como Product Owner. Las actividades principales incluyen:
#### Fase de Inicio: 
> Recolección de requisitos, creación del repositorio y firma de actas de entendimiento.
#### Fase de Diseño:
> Estructuración de la base de datos en archivos planos y diseño del menú de consola.
#### Fase de Desarrollo (fase 1):
> Implementación de módulos de Registro de Usuarios e Inventario con sus validaciones.
#### Fase de Desarrollo (fase 2):
> Lógica de préstamos, cálculo de facturación (impuesto del 23%) y generación de certificados .txt.
#### Fase de Cierre:
> Pruebas de seguridad del módulo administrador, exportación a CSV y redacción del manual de usuario.
## Cronograma
> El proyecto se desarrolla durante el semestre académico 2026-1, con hitos clave en las siguientes semanas:
#### Semana 1-7: 
> Planeación y Entrega 1 (Puntos 1 al 7).
#### Semana 8-15: 
> Codificación intensiva, pruebas y creación de la carpeta src y doc.
#### Semana 16: 
> Entrega final del software y sustentación ante el profesor.

![diagrama de gantt](https://raw.githubusercontent.com/sebastiankrios/Loans_Nicker/refs/heads/main/img/unnamed.png)

## Presupuesto
> Siguiendo las directrices académicas, el presupuesto no se mide en dinero real sino en "tiempo de práctica de formación".
#### Talento Humano: 
> 2 integrantes (Keiner y Nickolas).
#### Inversión de Tiempo: 
> siguiendo los parametros del cursum valor de horas de trabajo independiente invertidas al semestre es total de 80 horas*semestre de cada integrante.

![imagen de horas](https://raw.githubusercontent.com/sebastiankrios/Loans_Nicker/refs/heads/main/img/WhatsApp%20Image%202026-03-23%20at%209.22.58%20PM.jpeg)
#### Valorización: 
> Las horas se pagan simbólicamente al valor de una práctica profesional basada en 1 SMLV vigente.

>horas semanales practicante= 40;  semanas*mes= 4

>40*4= 160 horas al mes del practicante

>1,750,905/160 = 10,943 valor hora del practicante.

>10,943*80= 875,440 pago mensual a valor de practicantes por estudiantes.
# *Plan de versionado*
Versión,Día Aprox.,Semana,Hito / Procedimiento Relevante
>v0.1.0,Días 1 - 14,Sem 1-2
>"Inicio del proyecto: Creación del repositorio en GitHub, definición de integrantes, registro de actas de entendimiento y compromiso."
>v0.2.0,Días 15 - 35,Sem 3-5
>Definición técnica: Creación de la especificación de requisitos (funcionales y no funcionales) y el reporte de visión del proyecto.
>v0.5.0,Día 56,Sem 8
>"Entrega Avance 1: Consolidación del Plan de proyecto (Gantt, presupuesto), Plan de versionado y Puntos 1 al 7 finalizados."
Versión,Día Aprox.,Semana,Hito / Procedimiento Relevante
v0.6.0,Días 57 - 70,Sem 9-10,Estructura base: Creación de la carpeta src con el cascarón principal. Implementación del menú de consola interactivo y el registro/validación de usuarios.
v0.7.0,Días 71 - 84,Sem 11-12,"Módulos core: Desarrollo del registro de inventario, validaciones de categorías y lógica principal de Registrar Préstamo."
v0.8.0,Días 85 - 91,Sem 13,"Módulos avanzados: Implementación de Registrar Devolución, penalizaciones por ítems con más de 30 días e impresión de facturas y certificados en archivos .txt."
v0.9.0,Días 92 - 98,Sem 14,Administración y Documentación: Creación del panel de Administrador con sus reportes. Realización de pruebas lógicas. Creación de la carpeta doc con el manual de usuario.
Versión,Día Aprox.,Semana,Hito / Procedimiento Relevante
v0.9.5,Días 99 - 105,Sem 15,"Corrección de errores (Release Candidate): Ajustes finales tras probar todos los módulos, corrección de bugs en la lectura/escritura de archivos planos y optimización del código."
v1.0.0,Día 112,Sem 16,Entrega Definitiva (Producción): Software estable y completamente funcional con todas las carpetas (src y doc) cargadas en GitHub. Versión lista para la sustentación formal de los resultados.

