# FastAPI Blog CRUD Projects

This repository contains two complete implementations of a RESTful blog post CRUD API using FastAPI, demonstrating different ORM approaches and modern Python web development patterns.

## 📁 Project Structure

```
fastapi/
├── fastapi-sqlalchemy/        # Traditional SQLAlchemy ORM implementation
└── fastapi-sqlmodel/          # Modern SQLModel implementation
```

## 🚀 Projects Overview

### 1. fastapi-sqlalchemy
**Traditional ORM Approach with Proven Stability**

A complete RESTful API for managing blog posts built with established, battle-tested technologies.

**🔨 Tech Stack:**
- **FastAPI** – Modern web framework for building APIs
- **SQLAlchemy** – Traditional Python ORM for database interaction
- **Alembic** – Database migration and versioning tool
- **PostgreSQL** – Robust relational database
- **Pydantic** – Data validation for request/response schemas

**📂 Implementation Details:**
- **`models.py`**: SQLAlchemy `Post` model with `Base` inheritance
  - Fields: `id`, `title`, `content`, `writer`, `published`, `created_at`
- **`db.py`**: SQLAlchemy engine and session configuration with PostgreSQL
- **`routes.py`**: Complete CRUD endpoints using SQLAlchemy ORM query syntax
- **Alembic Integration**: Full migration setup with `alembic revision --autogenerate`

### 2. fastapi-sqlmodel
**Modern Type-Safe Approach with Simplified Development**

The same blog API rebuilt using SQLModel, showcasing modern Python development with enhanced type safety and reduced boilerplate.

**🔨 Tech Stack:**
- **FastAPI** – Modern web framework
- **SQLModel** – High-level ORM combining SQLAlchemy + Pydantic
- **Alembic** – Database migration tool (adapted for SQLModel)
- **PostgreSQL** – Relational database

**📂 Implementation Details:**
- **`models.py`**: Three SQLModel classes for different use cases:
  - `PostBase` – Base model with shared attributes
  - `Post` – model with all shared attributes(marked with `table=True`) 
  - `PostCreate` – Request validation model
  - `PostResponse` – Response model 
- **`db.py`**: Engine configuration with `Session(engine)` dependency injection
- **`routes.py`**: CRUD endpoints using SQLModel's `session.exec(select(Post))` syntax
- **Alembic Integration**: Custom setup with `SQLModel.metadata` and type handling

## 🔧 Complete CRUD API Endpoints

Both implementations provide identical REST API functionality:

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/post/` | Fetch all blog posts |
| `GET` | `/post/{id}` | Fetch a specific post by ID |
| `POST` | `/post/` | Create a new blog post |
| `PUT` | `/posts/{id}` | Update an existing post |
| `DELETE` | `/post/{id}` | Delete a post by ID |

## 🔍 Technical Comparison

| Aspect | fastapi-sqlalchemy | fastapi-sqlmodel |
|--------|-------------------|------------------|
| **Model Definition** | Single `Post` class with `Base` | Four classes: `PostBase`,`Post`, `PostCreate`, `PostResponse` |
| **Query Syntax** | Traditional SQLAlchemy ORM | Modern `session.exec(select())` |
| **Type Safety** | Separate Pydantic models needed | Built-in with SQLModel classes |
| **Validation** | Manual Pydantic schema creation | Automatic from SQLModel |
| **Alembic Setup** | Standard configuration | Custom metadata handling |
| **Code Complexity** | More boilerplate | Reduced boilerplate |
| **Learning Curve** | Steeper (separate concepts) | Gentler (unified approach) |
| **Maturity** | Battle-tested, extensive ecosystem | Newer, evolving |

## 🛠️ Getting Started

### Prerequisites
- Python 3.8+
- PostgreSQL database
- Git

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd fastapi
   ```

2. **Choose your implementation and navigate:**
   ```bash
   # For SQLAlchemy version
   cd fastapi-sqlalchemy
   
   # OR for SQLModel version
   cd fastapi-sqlmodel
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Database Configuration:**
   - Create a PostgreSQL database
   - Update the connection string in `db.py`

5. **Run database migrations:**
   ```bash
   # Initialize Alembic (if not already done)
   alembic init alembic
   
   # Generate migration
   alembic revision --autogenerate -m "Create posts table"
   
   # Apply migrations
   alembic upgrade head
   ```

6. **Start the application:**
   ```bash
   uvicorn main:app --reload
   ```

7. **Access your API:**
   - **API Base:** `http://localhost:8000`
   - **Interactive Docs:** `http://localhost:8000/docs`
   - **Alternative Docs:** `http://localhost:8000/redoc`

## 🏗️ Architecture Highlights

### FastAPI-SQLAlchemy Architecture
- **Separation of Concerns**: Clear distinction between ORM models and API schemas
- **Traditional Patterns**: Uses established SQLAlchemy query patterns
- **Flexibility**: Fine-grained control over database operations

### FastAPI-SQLModel Architecture
- **Unified Models**: Single source of truth for data structures
- **Type Safety**: Automatic validation and serialization
- **Modern Syntax**: Cleaner, more readable query syntax
- **Dependency Injection**: Elegant session management with FastAPI's `Depends()`

## 🧪 Key Learning Outcomes

From building these projects, you've mastered:

- ✅ **RESTful API Design** with FastAPI
- ✅ **Database Integration** with PostgreSQL
- ✅ **ORM Usage** in both traditional and modern approaches
- ✅ **Migration Management** with Alembic for both ORMs
- ✅ **Dependency Injection** patterns
- ✅ **Type Safety** and validation strategies
- ✅ **Project Structuring** with modular design (`models`, `db`, `routes`)
- ✅ **Advanced Schema Generation** with timestamps and defaults

## 🎯 When to Use Each Approach

### Choose `fastapi-sqlalchemy` when:
- Working with existing SQLAlchemy codebases
- Need complex database operations and advanced ORM features
- Require maximum flexibility and control
- Team has extensive SQLAlchemy experience
- Building enterprise applications with complex requirements

### Choose `fastapi-sqlmodel` when:
- Starting new FastAPI projects
- Want reduced boilerplate and faster development
- Prefer type-safe code with automatic validation
- Building APIs where models closely match database tables
- Team values modern Python development practices

## 📚 Technologies & Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [SQLModel Documentation](https://sqlmodel.tiangolo.com/)
- [Alembic Documentation](https://alembic.sqlalchemy.org/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)

## 🤝 Contributing

Both implementations are fully functional and demonstrate different approaches to the same problem. Feel free to:
- Compare implementation strategies
- Extend functionality
- Add new features
- Improve existing code

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

**Explore both approaches and discover which fits your development style! 🚀**
