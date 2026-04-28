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

Create `.env
