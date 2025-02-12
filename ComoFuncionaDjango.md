# Cómo Funciona Django: Guía Rápida

## Introducción

Django es un framework de desarrollo web de alto nivel en Python que fomenta el desarrollo rápido, limpio y pragmático. Sigue el patrón de diseño Modelo-Vista-Template (MVT), que es esencialmente una variante del MVC (Modelo-Vista-Controlador).

## 1. Instalación

### Prerrequisitos

*   **Python:** Django requiere Python. Se recomienda usar la última versión estable.
*   **pip:** El gestor de paquetes de Python.

### Pasos

1.  **Crear un entorno virtual (recomendado):**

    ```bash
    python -m venv venv
    ```

    Esto crea un entorno aislado para tu proyecto.
2.  **Activar el entorno virtual:**

    *   En Windows:

        ```bash
        venv\Scripts\activate
        ```

    *   En macOS/Linux:

        ```bash
        source venv/bin/activate
        ```
3.  **Instalar Django:**

    ```bash
    pip install django
    ```
4.  **Verificar la instalación:**

    ```bash
    django-admin --version
    ```

## 2. Crear un Proyecto

1.  **Crear el proyecto:**

    ```bash
    django-admin startproject myproject
    ```

    Esto crea un directorio `myproject` con la estructura básica del proyecto.
2.  **Estructura del proyecto:**

    ```
    myproject/
    ├── manage.py
    └── myproject/
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        ├── asgi.py
        └── wsgi.py
    ```

## 3. Ejecutar el Servidor de Desarrollo

1.  **Navegar al directorio del proyecto:**

    ```bash
    cd myproject
    ```
2.  **Ejecutar el servidor:**

    ```bash
    python manage.py runserver
    ```

    Por defecto, el servidor se ejecuta en `http://127.0.0.1:8000/`.

## 4. Crear una App

1.  **Crear la app:**

    ```bash
    python manage.py startapp tasks
    ```

    Esto crea un directorio `tasks` con la estructura básica de la app.
2.  **Estructura de la app:**

    ```
    tasks/
    ├── migrations/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    └── views.py
    ```

## 5. Ficheros y su Función (General)

*   **manage.py:** Script para administrar el proyecto (ejecutar servidor, crear migraciones, etc.).
*   **settings.py:** Configuración del proyecto (base de datos, apps instaladas, middleware, etc.).
*   **urls.py:** Define las URL del proyecto (mapea las URLs a las vistas).
*   **wsgi.py/asgi.py:** Configuración para desplegar la app en un servidor WSGI/ASGI.
*   **models.py:** Define la estructura de la base de datos (modelos).
*   **views.py:** Contiene la lógica de la aplicación (vistas).
*   **admin.py:** Configura el panel de administración de Django.
*   **apps.py:** Configuración de la app.
*   **migrations/:** Almacena los cambios en la base de datos (migraciones).

## 6. Ficheros y su Función (App tasks)

*   **models.py:** Define el modelo `Task` (título, completado).
*   **views.py:** Contiene las vistas para listar, crear, marcar como hecha y borrar tareas.
*   **urls.py:** Define las URLs específicas de la app `tasks`.
*   **admin.py:** Permite administrar las tareas desde el panel de administración de Django.
*   **migrations/:** Almacena los cambios en la base de datos (en este caso, la creación del modelo `Task`).

## 7. Uso de HTMX y Tailwind

*   **HTMX:** Permite crear interfaces de usuario dinámicas sin usar JavaScript. Se usa para marcar tareas como hechas y borrarlas sin recargar la página.
*   **Tailwind CSS:** Framework CSS para estilizar la interfaz de usuario de forma rápida y sencilla.

## 8. Configuración del Proyecto (App tasks)

1.  **Añadir la app a `settings.py`:**

    ```python
    INSTALLED_APPS = [
        ...,
        'tasks',
    ]
    ```

2.  **Definir el modelo en `models.py`:**

    ```python
    from django.db import models

    class Task(models.Model):
        title = models.CharField(max_length=255)
        completed = models.BooleanField(default=False)

        def __str__(self):
            return self.title
    ```
3.  **Crear migraciones:**

    ```bash
    python manage.py makemigrations tasks
    python manage.py migrate
    ```
4.  **Definir las vistas en `views.py`:**

    ```python
    from django.shortcuts import render, get_object_or_404, redirect
    from django.http import HttpResponse
    from .models import Task

    def task_list(request):
        tasks = Task.objects.all()
        return render(request, "tasks/task_list.html", {"tasks": tasks})

    def toggle_task(request, task_id):
        task = get_object_or_404(Task, id=task_id)
        task.completed = not task.completed
        task.save()
        return render(request, "tasks/partials/task_item.html", {"task": task})

    def delete_task(request, task_id):
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        return HttpResponse("")

    def add_task(request):
        if request.method == "POST":
            title = request.POST.get("title")
            if title:
                Task.objects.create(title=title)
        tasks = Task.objects.all()
        return render(request, "tasks/partials/task_list.html", {"tasks": tasks})
    ```

5.  **Definir las URLs en `urls.py`:**

    ```python
    from django.urls import path
    from .views import task_list, toggle_task, delete_task, add_task

    urlpatterns = [
        path("", task_list, name="task_list"),
        path("toggle/<int:task_id>/", toggle_task, name="toggle_task"),
        path("delete/<int:task_id>/", delete_task, name="delete_task"),
        path("add/", add_task, name="add_task"),
    ]
    ```

6.  **Crear las plantillas HTML:**

    *   `tasks/templates/tasks/task_list.html`: Plantilla principal para listar las tareas.
    *   `tasks/templates/tasks/partials/task_item.html`: Plantilla parcial para mostrar cada tarea individualmente.

## 9. Conclusión

Con esto, tendrás una aplicación Django funcional para gestionar tareas, usando HTMX y Tailwind CSS para una experiencia de usuario moderna y ágil.