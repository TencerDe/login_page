# Authentication System – Project Overview

## Introduction

This project implements a custom authentication system built using Django. The goal is to design a production-ready identity and security architecture instead of relying entirely on Django’s default authentication behavior.

The system is structured to be scalable, secure, and easy for future contributors to understand and extend.

---

## Work Completed So Far

### 1. Custom User Model

A fully customized user model has been created to replace Django’s default user.

**Key Decisions:**

* Username has been removed.
* Email is the primary identifier (`USERNAME_FIELD`).
* A custom user manager is implemented to support email-based user and superuser creation.
* Verification state is tracked using an `is_verified` flag.
* UUID is used as the primary key for improved security and non-predictability.
* Admin is configured to properly manage the custom user.

**Purpose:**
Establish a strong identity layer that supports modern authentication practices.

---

### 2. Custom User Manager

A custom manager handles:

* User creation using email
* Superuser creation with proper permission flags
* Email normalization
* Secure password handling

**Reason:**
Django’s default manager expects a username. Since the system uses email-only authentication, a custom manager is required.

---

### 3. Admin Configuration

The Django admin panel has been configured to support the custom user model.

**Features:**

* Custom creation and change forms
* Email-based search
* Proper permission fields
* Verification visibility
* Logical ordering

**Goal:**
Ensure internal operators can safely manage users without friction.

---

## Phase 2 – Authentication Database Design

The project is currently focused on building the security data layer before implementing API logic.

### Email Verification Token Model

This model supports magic-link based email verification.

**Design Principles:**

* Tokens are temporary security events.
* Tokens must expire.
* Tokens must be single-use.
* New tokens invalidate older ones.

**Fields:**

* `user` – ForeignKey to the custom user
* `token` – unique verification string
* `created_at` – timestamp of generation
* `expires_at` – expiry timestamp
* `is_used` – prevents reuse

**Behavior Strategy:**

* Multiple tokens per user are allowed.
* When a new token is generated, previous unused tokens should be invalidated.
* Tokens are intended to be deleted or cleaned periodically.

---

## Architectural Philosophy

The authentication system follows a layered approach:

**Identity Layer**

* CustomUser

**Trust Layer**

* EmailVerificationToken

Upcoming layers will include:

* Session / Refresh Token tracking
* Password reset tokens
* Authorization controls
* Security hardening

The database is designed before writing authentication APIs to prevent schema refactors later.

---

## Current Status

Completed:

* Custom User Model
* Custom Manager
* Admin Integration
* Email Verification Token Schema

In Progress:

* Session / Refresh Token Model

Planned:

* Password Reset Model
* Signup flow
* Magic link verification flow
* Login system
* Token lifecycle management
* Logout mechanisms
* Authorization
* Rate limiting
* Production security practices

---

## Contribution Guidelines

Before contributing:

1. Follow existing architectural patterns.
2. Avoid introducing authentication logic without schema consideration.
3. Keep models minimal and purpose-driven.
4. Do not mix temporary security data with identity models.
5. Maintain clear naming conventions.

When adding new authentication features, design the data model first.

---

## Project Goal

The objective of this project is to build a backend authentication system that reflects real-world engineering practices rather than tutorial-level implementations.

The focus is on:

* Security
* Scalability
* Clean architecture
* Operational clarity

Future contributors should aim to preserve these principles.


# Project Folder Structure Guide

## Purpose

This guide explains how the project is organized so contributors can quickly understand where code belongs and how to extend the system without breaking architectural consistency.

The structure prioritizes clarity, scalability, and separation of concerns.

---

## Root Directory Overview

```
login/
│
├── accounts/
├── core/
├── login/#(This is the main app having all necessary configed files)
├── manage.py
├── requirements.txt
└── README.md
```

---

## accounts/ (Identity and Authentication Domain)

This is the most critical app in the project. Everything related to authentication and user security must live here.

```
accounts/
│
├── migrations/
├── admin.py
├── apps.py
├── forms.py
├── managers.py
├── models.py
├── views.py        (future APIs)
├── serializers.py  (future DRF usage)
├── services/       (recommended for business logic)
└── tests/
```

### Responsibilities

* Custom user model
* Verification tokens
* Session / refresh tokens
* Password reset tokens
* Authentication logic
* Authorization helpers

### Important Rule

Do NOT split authentication into multiple apps unless the domain becomes independently deployable.

Auth should remain centralized.

---

## Recommended Internal Structure (accounts)

As the project grows, avoid placing all logic inside `views.py` or `models.py`.

Introduce a service layer.

Example:

```
accounts/
│
├── services/
│   ├── user_service.py
│   ├── token_service.py
│   ├── email_service.py
│   └── session_service.py
```

### Why This Matters

Views should handle HTTP.

Services should handle business logic.

This prevents fat views and keeps the system maintainable.

---

## managers.py

Move custom managers here instead of keeping them inside `models.py`.

Example responsibilities:

* CustomUserManager
* Token creation helpers
* Query utilities

This keeps models clean and easier to read.

---

## tests/

Every authentication feature should eventually have tests.

Recommended structure:

```
tests/
├── test_user_model.py
├── test_verification.py
├── test_sessions.py
└── test_auth_flow.py
```

Security systems without tests are fragile.

---

## project_core/ (Project Configuration)

This folder contains global configuration.

```
project_core/
│
├── __init__.py
├── asgi.py
├── settings.py
├── urls.py
└── wsgi.py
```

### Keep It Clean

Avoid placing business logic here.

Only configuration belongs in this directory.

---

## Future Apps (When Needed)

Create new apps only when the domain is clearly separate.

Examples:

### payments/

Handles financial workflows.

### notifications/

Centralized email, SMS, push infrastructure.

### products/ or core/

Business-specific logic unrelated to identity.

---

## Architectural Rules

### 1. Group by Domain, Not Feature

Authentication belongs in one place.

Avoid structures like:

* users/
* tokens/
* verification/

Keep them inside `accounts`.

---

### 2. Keep Models Minimal

Models should store data — not business workflows.

---

### 3. Avoid Circular Dependencies

Centralizing auth prevents import chaos later.

---

### 4. Prefer Explicit Naming

Bad:

```
utils.py
helpers.py
misc.py
```

Good:

```
token_service.py
email_sender.py
session_manager.py
```

Clarity scales.

---

## Growth-Oriented Structure (Future)

As traffic and complexity increase, the architecture should naturally support:

* background workers
* async email sending
* audit logging
* device tracking
* security monitoring

Design today so expansion does not require rewrites.

---

## Contributor Expectations

When adding new features:

1. Identify the domain first.
2. Decide whether it belongs inside `accounts`.
3. Design database schema before APIs.
4. Keep business logic out of views.
5. Follow existing naming patterns.

Consistency is more important than creativity in backend systems.

---

## Summary

This project follows a domain-driven structure with authentication as a centralized service.

The goal is to maintain:

* predictable architecture
* secure design
* readable codebase
* scalable structure

Future contributors should prioritize simplicity and avoid premature complexity.


