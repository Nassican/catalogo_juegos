# Catálogo de Juegos 🎮

Una aplicación web moderna desarrollada con Django para gestionar y explorar un catálogo de videojuegos, permitiendo a los usuarios registrar juegos, escribir reseñas y gestionar categorías.

## 🚀 Características

- 👤 Sistema de autenticación y registro de usuarios
- 🎮 Gestión completa de juegos (CRUD)
- ⭐ Sistema de reseñas y valoraciones
- 🏷️ Categorización de juegos
- 📱 Interfaz responsive y moderna
- 👑 Panel de administración especializado

## 🛠️ Tecnologías Utilizadas

- Django 5.1.2
- Python 3.11
- Bootstrap
- AdminLTE3
- SQLite
- Docker
- Font Awesome

## 📋 Prerrequisitos

- Docker y Docker Compose
- Python 3.11 o superior (para desarrollo local)
- pip (gestor de paquetes de Python)

## 🔧 Instalación

1. Clonar el repositorio:

```
bash
git clone https://github.com/tuusuario/catalogo_juegos.git
cd catalogo_juegos
```

2. Construir y levantar los contenedores:

```
bash
docker-compose up --build
```

3. Acceder a la aplicación:

```
http://localhost:8000
```

## 💻 Desarrollo Local

1. Crear un entorno virtual:

```
bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

2. Instalar dependencias:

```
bash
pip install -r requirements.txt
```

3. Realizar migraciones:

```
bash
python manage.py migrate
```

4. Crear superusuario:

```
bash
python manage.py createsuperuser
```

5. Iniciar servidor de desarrollo:

```
bash
python manage.py runserver
```

## 📁 Estructura del Proyecto

```
catalogo_juegos/
├── catalogo_juegos/    # Configuración principal del proyecto
├── juegos/             # Aplicación principal
├── media/             # Archivos subidos por usuarios
├── static/            # Archivos estáticos
├── templates/         # Plantillas HTML
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## 👥 Roles de Usuario

- **Administrador**: Gestión completa del catálogo y usuarios
- **Usuario**: Puede escribir reseñas y gestionar su perfil

## 🔐 Variables de Entorno

- `DEBUG`: Modo debug (1 o 0)
- `DJANGO_SETTINGS_MODULE`: Módulo de configuración
- `SECRET_KEY`: Clave secreta de Django

## 📝 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE.md](LICENSE.md) para detalles

## ✨ Contribuir

1. Fork el proyecto
2. Crea tu rama de características (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request
```