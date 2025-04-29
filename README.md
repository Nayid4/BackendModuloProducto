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

## 🧑‍💻 Autor

**Nayid Junior Castellar Agamez**  
