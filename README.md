# user-crud-monitoring

# User Management API with Monitoring

## Descripción

Este proyecto implementa una **API RESTful** para la gestión de usuarios utilizando **FastAPI**. La API permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre los usuarios, donde cada usuario tiene atributos como `id`, `nombre`, `edad`, y `email`.

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


