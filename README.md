# 🛠️ API de Gestión de Inventario de Productos

Esta API permite crear productos, listar todos los productos registrados y generar alertas cuando el stock esté por debajo del mínimo. Diseñada bajo principios de Clean Architecture e implementada con Flask y SQLAlchemy.

---

## ▶️ Iniciar servidor

```bash
python main.py
```

Servidor correrá en: `http://127.0.0.1:5000`

---

## 📚 Endpoints

| Método | Ruta               | Descripción                            |
|--------|--------------------|----------------------------------------|
| GET    | `/products`        | Listar todos los productos             |
| POST   | `/products`        | Crear un nuevo producto                |
| GET    | `/products/alerts` | Listar productos con stock bajo mínimo |

### 📥 Ejemplo JSON para `POST /products`

```json
{
  "name": "Teclado",
  "code": "SKU12345",
  "stock": 10,
  "min_stock": 20
}
```

---

## 🧱 Estructura de Carpetas

```bash
.
GestionDeProductos/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── domain/
│   │   ├── __init__.py
│   │   ├── entities/
│   │   │   └── product.py
│   │   └── repositories/
│   │       └── product_repository.py
│   ├── infrastructure/
│   │   ├── __init__.py
│   │   └── database/
│   │       ├── __init__.py
│   │       ├── models.py
│   │       ├── db_context.py
│   │       └── unit_of_work.py
│   ├── application/
│   │   ├── __init__.py
│   │   └── services/
│   │       ├── __init__.py
│   │       ├── product_commands.py
│   │       └── product_queries.py
│   ├── interfaces/
│   │   └── routes.py
│
├── tests/
│   └── test_product.py
│
├── requirements.txt
└── README.md
```

---

## 🧪 Ejecutar tests

```bash
pytest
```

---

## 📌 Tecnologías utilizadas

- Python 3.10+
- Flask
- SQLAlchemy
- SQLite
- Pytest

---

## Parte 2: Preguntas Conceptuales

### 1. Diseño y Arquitectura

**¿Cómo diseñarías un sistema tipo MRP modular y escalable que permita añadir funcionalidades como predicción de demanda o reportes BI en el futuro? ¿Qué patrón(es) o arquitectura usarías y por qué?**

Diseñaría un sistema MRP usando una combinación de **Domain-Driven Design (DDD)**, **arquitectura hexagonal** y una orientación hacia **microservicios**. Esta arquitectura me ha permitido, en proyectos anteriores, construir soluciones bien alineadas con el negocio, fáciles de escalar y mantener.

- **DDD** ayuda a capturar las reglas del negocio de forma precisa, lo que facilita el crecimiento modular del sistema sin comprometer su coherencia.
- **La arquitectura hexagonal** (Ports and Adapters) desacopla el núcleo del sistema de detalles técnicos como bases de datos o frameworks, permitiendo cambiar tecnologías o añadir nuevas funcionalidades como predicción de demanda o BI sin afectar la lógica principal.
- **Microservicios o módulos desacoplados** permiten escalar partes críticas como los reportes o análisis predictivo, usando colas de eventos (como **RabbitMQ** o **Kafka**) y patrones como Event Sourcing para una trazabilidad efectiva del estado.

Esta aproximación está basada en mi experiencia desarrollando sistemas distribuidos, aplicando principios SOLID, arquitectura limpia y patrones como Strategy, Repository y Factory.

---

### 2. Gestión de Datos y Eficiencia

**Supón que el sistema MRP debe manejar miles de productos y transacciones por día. ¿Qué estrategias de diseño y herramientas aplicarías para asegurar un rendimiento óptimo en consultas, validaciones y alertas relacionadas con el inventario?**

Para garantizar eficiencia y rendimiento, aplicaría varias estrategias que ya he implementado en proyectos anteriores:

- **Índices bien diseñados** en columnas claves como `codigoProducto`, `stockActual`, `stockMinimo` para mejorar tiempos de respuesta.
- **Consultas optimizadas** y uso de **paginación** (`LIMIT`, `OFFSET`) para controlar la carga de datos.
- Validaciones de negocio implementadas en la **capa de dominio**, evitando lógica duplicada en otras capas.
- **Caching** con **Redis** para datos frecuentemente consultados, como catálogos de productos.
- Procesamiento de tareas intensivas (como alertas de stock) mediante **eventos asíncronos**.
- Implementación de **vistas materializadas** para analítica y generación de reportes.
- Monitoreo constante del rendimiento con herramientas como **Grafana**, **Prometheus** y **ELK Stack**, para detectar cuellos de botella y tomar decisiones con datos.

Estas soluciones reflejan mi enfoque práctico orientado a resultados, aplicando herramientas modernas como Docker, SonarQube y GitHub Actions para integraciones y despliegues.

---

### 3. Lógica de Programación

**Escribe una función que reciba una lista de números enteros y retorne el primer número que no se repite.**

#### Solución en Python:

```python
def primer_no_repetido(lista):
    conteo = {}
    for numero in lista:
        conteo[numero] = conteo.get(numero, 0) + 1
    for numero in lista:
        if conteo[numero] == 1:
            return numero
    return None
```


## 🧑‍💻 Autor

**Nayid Junior Castellar Agamez**  
