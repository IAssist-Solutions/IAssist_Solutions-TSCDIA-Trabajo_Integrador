# IAssist_Solutions-TSCDIA-Trabajo_Integrador

## Integrantes del grupo
* Mario Arce | 39302448 | marioezequielarce95@gmail.com | https://github.com/Marioarce95
* Emilce Robles | 37093958 | emi.nrobles@gmail.com | https://github.com/emirobles 
* Jenifer De Piano | 41087669 | jeniferyamila@hotmail.com | https://github.com/JENIF3R1

## Descripción de la Propuesta del Proyecto
Nombre del Proyecto: Sistema de Gestión de Hábitos

### Objetivo del Proyecto:
Desarrollar una aplicación web que permita a los usuarios gestionar y seguir sus hábitos diarios, categorizarlos y registrar sus progresos. El sistema ofrecerá funcionalidades para crear, visualizar y analizar hábitos, así como registrar y revisar el historial de actividades relacionadas con esos hábitos.
Justificación:
La gestión de hábitos es una herramienta clave para el desarrollo personal y la productividad. Un sistema que permita a los usuarios registrar sus hábitos, clasificarlos y hacer seguimiento de su progreso proporcionará una estructura valiosa para quienes buscan mejorar sus rutinas diarias. La aplicación ofrecerá una solución centralizada y accesible para el seguimiento de hábitos, contribuyendo así al bienestar y la eficiencia personal de los usuarios.

### Alcance del Proyecto:
El proyecto contempla el diseño, desarrollo y despliegue de una aplicación web con las siguientes características principales:
1.	Gestión de Usuarios:
*	Registro de usuarios.
*	Autenticación y gestión de sesiones.
*	Perfil de usuario.
2.	Gestión de Hábitos:
*	Creación, edición y eliminación de hábitos.
*	Asignación de hábitos a categorías.
*	Establecimiento de fechas de inicio para los hábitos.
3.	Categorías:
*	Creación, edición y eliminación de categorías.
*	Clasificación de hábitos dentro de categorías específicas.
4.	Registro de Actividades:
*	Registro diario de actividades relacionadas con los hábitos.
*	Visualización del historial de registros.
*	Análisis y seguimiento del progreso de los hábitos.

### Diagrama Entidad-Relación (ER) en Notación de Chen:
![Diagrama Entidad Relacion](https://github.com/IAssist-Solutions/IAssist_Solutions-TSCDIA-Trabajo_Integrador/blob/main/DER.PNG)

Entidades y Atributos:
1.	Entidad User (Usuario):
*	Atributos:
*	user_id (PK)
*	username
*	email
*	password

2.	Entidad Habit (Hábito):
*	Atributos:
*	habit_id (PK)
*	name
*	description
*	start_date

3.	Entidad Category (Categoría):
*	Atributos:
*	category_id (PK)
*	category_name

4.	Entidad HabitLog (Registro de Hábitos):
*	Atributos:
*	log_id (PK)
*	log_date

### Relaciones y Cardinalidades:
1.	Relación User-Habit (Has):
*	Descripción: Un usuario puede tener múltiples hábitos.
*	Cardinalidad:
*	1 a N (Un usuario puede tener muchos hábitos)
*	N a 1 (Un hábito pertenece a un solo usuario)

2.	Relación Habit-Category (BelongsTo):
*	Descripción: Un hábito pertenece a una categoría.
*	Cardinalidad:
*	1 a 1 (Cada hábito pertenece a una categoría)
*	N a 1 (Una categoría puede tener muchos hábitos)

3.	Relación User-HabitLog (Logs):
*	Descripción: Un usuario puede registrar múltiples logs.
*	Cardinalidad:
*	1 a N (Un usuario puede registrar muchos logs)
*	N a 1 (Un log pertenece a un solo usuario)

4.	Relación Habit-HabitLog (Records):
*	Descripción: Un log se relaciona con un hábito.
*	Cardinalidad:
*	1 a N (Un hábito puede tener muchos registros de logs)
*	N a 1 (Un log se asocia a un solo hábito)
