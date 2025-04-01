# user-crud-monitoring

# User Management API with Monitoring

## Descripción

Este proyecto implementa una **API RESTful** para la gestión de usuarios utilizando **FastAPI**. La API permite realizar operaciones CRUD (Crear, obtener) sobre los usuarios, donde cada usuario tiene atributos como `id`, `nombre`, `edad`.

Adicionalmente, se integra con **Prometheus** para monitorear las métricas relacionadas con la creación de usuarios y otros aspectos clave del rendimiento del sistema, como la latencia de las solicitudes. **Grafana** se utiliza para visualizar las métricas recolectadas en tiempo real, permitiendo un monitoreo y análisis eficientes de la aplicación.

## Explicación del Proyecto

Este proyecto proporciona una API sencilla para gestionar usuarios. Sus funcionalidades principales incluyen:
- **Crear usuarios**: Permite añadir nuevos usuarios a la base de datos.
- **Obtener usuarios**: Consulta todos los usuarios existentes en la base de datos.
- **Monitoreo con Prometheus**: Registra métricas sobre la creación de usuarios y otros aspectos clave del sistema.
- **Dashboard en Grafana**: Visualiza las métricas recolectadas, como el número de usuarios creados y la latencia de las solicitudes.

## Justificación del Proyecto

La gestión de usuarios es esencial en muchas aplicaciones modernas, y su monitoreo es clave para asegurar un rendimiento adecuado. Este proyecto no solo facilita la gestión de usuarios, sino que también proporciona un sistema robusto de monitoreo utilizando **Prometheus** y **Grafana**, lo que ayuda a detectar posibles problemas de rendimiento de manera temprana.

Además, la integración con **FastAPI** permite una implementación rápida y eficiente de la API con soporte para validación automática y documentación interactiva.

El propósito principal del proyecto es:
1. **Mejorar la gestión de usuarios** mediante una API robusta y fácil de usar.
2. **Monitorear el sistema** para asegurar un rendimiento óptimo y reducir los riesgos de problemas de rendimiento.

## Tecnologías Utilizadas

- **FastAPI**: Framework para la creación de la API RESTful.
- **Prometheus**: Herramienta de monitoreo para recolectar y almacenar métricas.
- **Grafana**: Herramienta de visualización para mostrar las métricas en tiempo real.

## Instalación

1. Clona este repositorio:
   ```bash
   git clone <url_del_repositorio>

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt


**Aviso importante**

Este proyecto utiliza **Docker Compose** para orquestar todos los servicios, incluyendo **FastAPI**, **PostgreSQL**, **Prometheus**, y **Grafana**.

1. **Docker**: Asegúrate de tener Docker instalado en tu máquina. Si no lo tienes, puedes instalarlo desde [aquí](https://docs.docker.com/get-docker/).
2. **Docker Compose**: Asegúrate de tener Docker Compose instalado. Si no lo tienes, sigue las instrucciones de instalación en [Docker Compose](https://docs.docker.com/compose/install/).


3. Construir y ejecutar los contenedores con Docker Compose: En la raíz del proyecto, donde se encuentra el archivo docker-compose.yml, ejecuta el siguiente comando para construir y levantar todos los contenedores:
   ```bash
    docker-compose up --build


Este comando hará lo siguiente:

Construirá las imágenes de Docker necesarias.

Levantará los contenedores para FastAPI, PostgreSQL, Prometheus, y Grafana.

4. Acceder a la aplicación: Una vez que los contenedores estén en ejecución, puedes acceder a las diferentes aplicaciones a través de los siguientes puertos:


Prometheus: http://localhost:9090

Grafana: http://localhost:3000 (credenciales predeterminadas: admin / admin)


5. Verificar que todo funcione correctamente:


   ```bash
       docker ps


Verifica que el servicio de FastAPI esté corriendo correctamente accediendo a la ruta de la documentación en http://localhost:8000/docs.

En Prometheus, verifica que las métricas de FastAPI estén siendo recolectadas correctamente en http://localhost:9090/targets.

En Grafana, verifica que Prometheus esté configurado como fuente de datos y que las métricas de FastAPI se estén visualizando correctamente en el dashboard.