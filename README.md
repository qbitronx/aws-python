# Flask MVC — Developer Profile

Aplicación web MVC con Python Flask que muestra el perfil de un desarrollador.

## Estructura del proyecto

```
aws-python/
├── app/
│   ├── __init__.py
│   ├── controllers/
│   │   └── developer_controller.py
│   └── models/
│       └── developer.py
├── templates/
│   └── index.html
├── static/
│   └── css/style.css
├── run.py
├── requirements.txt
├── Dockerfile
└── README.md
```

## Ejecución local

### 1. Clonar el repositorio

```bash
git clone <repo-url>
cd aws-python
```

### 2. Crear y activar el entorno virtual

```bash
python3 -m venv venv
source venv/bin/activate        # macOS / Linux
# venv\Scripts\activate         # Windows
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación

```bash
python run.py
```

Abre el navegador en: [http://localhost:5000](http://localhost:5000)

---

## Ejecución con Docker

### 1. Construir la imagen

```bash
docker build -t flask-developer-profile .
```

### 2. Ejecutar el contenedor

```bash
docker run -p 5000:5000 flask-developer-profile
```

Abre el navegador en: [http://localhost:5000](http://localhost:5000)

### 3. Detener el contenedor

```bash
docker ps                          # obtener CONTAINER_ID
docker stop <CONTAINER_ID>
```
