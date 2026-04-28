# Smart E-Commerce Backend + AI Product Recommendation

Production-ready backend portfolio project built with **FastAPI**, **PostgreSQL**, **Redis**, **Celery**, **Docker**, and a simple **AI recommendation engine**.

This project simulates a scalable e-commerce backend architecture with authentication, product management, checkout flow, caching, async tasks, recommendation system, CI/CD, and deployment-ready setup.

---

## Features

### Authentication

* User registration
* User login
* JWT authentication
* Protected routes
* Password hashing using bcrypt

### Product Management

* Product CRUD
* Category CRUD
* Product filtering
* Pagination

### Cart System

* Add to cart
* Update quantity
* Remove product
* View cart items

### Checkout System

* Order creation
* Order items creation
* Transaction-safe checkout
* Automatic cart cleanup

### Redis Caching

* Product caching
* Category caching
* Cache invalidation strategy

### AI Recommendation Engine

* Track user behavior
* Recommendation logs
* Content-based product recommendation

### Background Jobs

* Async order confirmation using Celery
* Redis as message broker

### DevOps

* Dockerized services
* Docker Compose setup
* GitHub Actions CI pipeline

---

# Tech Stack

* FastAPI
* PostgreSQL
* SQLAlchemy
* Alembic
* Redis
* Celery
* Docker
* Docker Compose
* GitHub Actions
* Pytest

---

# Project Architecture

```bash
app/
│
├── api/
├── core/
├── db/
├── models/
├── repositories/
├── schemas/
├── services/
├── workers/
│
└── main.py
```

---

# System Architecture

```bash
Client
   ↓
FastAPI API Layer
   ↓
Service Layer
   ↓
Repository Layer
   ↓
PostgreSQL

Redis → caching
Celery → background jobs
Recommendation Engine → AI personalization
Docker → deployment
GitHub Actions → CI/CD
```

---

# Database Schema

### users

* id
* email
* password

### categories

* id
* name

### products

* id
* name
* description
* price
* category_id

### cart_items

* id
* user_id
* product_id
* quantity

### orders

* id
* user_id
* total_price

### order_items

* id
* order_id
* product_id
* quantity
* price

### recommendation_logs

* id
* user_id
* product_id
* action_type
* created_at

---

# Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/smart-ecommerce-backend.git
cd smart-ecommerce-backend
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Activate:

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create `.env`

```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/ecommerce
SECRET_KEY=your_secret_key
ALGORITHM=HS256
REDIS_HOST=localhost
REDIS_PORT=6379
```

---

# Run Application

```bash
uvicorn app.main:app --reload
```

Swagger Docs:

```bash
http://localhost:8000/docs
```

---

# Run Docker

```bash
docker-compose up --build
```

---

# Run Database Migration

```bash
alembic upgrade head
```

---

# Run Celery Worker

```bash
celery -A app.workers.tasks worker --loglevel=info
```

---

# API Endpoints

## Auth

* POST `/auth/register`
* POST `/auth/login`

## Products

* GET `/products`
* POST `/products`

## Categories

* GET `/categories`
* POST `/categories`

## Cart

* POST `/cart`
* PUT `/cart/{product_id}`
* DELETE `/cart/{product_id}`
* GET `/cart`

## Orders

* POST `/orders/checkout`

## Recommendation

* GET `/recommendations`

---

# CI/CD

GitHub Actions automatically:

* Install dependencies
* Run tests
* Validate build

Workflow file:

```bash
.github/workflows/ci.yml
```

---

# Deployment

Recommended platforms:

* Railway
* Render
* Fly.io

Live API:

```bash
https://your-app-url.com
```

---

# Future Improvements

* Payment gateway integration
* Elasticsearch product search
* Kafka event streaming
* Kubernetes deployment
* Advanced ML recommendation model

---

# Testing Status (Important Note)

⚠️ Automated testing is currently **partially implemented**.

Pytest setup has been added for:

* Auth testing
* Product testing
* Checkout testing

However, some tests are still experiencing issues due to:

* Test database isolation
* Redis mocking
* Celery async task mocking
* Integration environment configuration

This is currently being improved in future iterations.

The core application features are fully functional and manually tested through Swagger/Postman.

---

# Why This Project?

This project was built to demonstrate backend engineering skills beyond basic CRUD applications by implementing:

* scalable architecture
* caching strategy
* asynchronous processing
* transactional checkout logic
* recommendation system
* containerization
* CI/CD pipeline

This project is intended as a portfolio project for Backend Engineer roles.
