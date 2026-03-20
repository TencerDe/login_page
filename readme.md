Authentication System – Updated Project README (Phase 1 → Phase 4)
Introduction

This project implements a production-ready authentication system using Django and Django REST Framework.

The system is designed from scratch instead of relying fully on Django’s default authentication to ensure:

Clean architecture

Strong security practices

Scalability for real-world applications

Architecture Overview

The project follows a strict layered architecture:

APIView (Controller)
    ↓
Serializer (Validation)
    ↓
Service Layer (Business Logic)
    ↓
Manager (Low-level operations)
    ↓
Model (Database)

This separation ensures maintainability and avoids tightly coupled code.

Phase 1 – Custom User System (Completed)
Features Implemented

Custom user model using email as primary identifier

Username removed

UUID as primary key

is_verified flag for email verification

Custom user manager for user and superuser creation

Django admin fully configured

Purpose

Create a flexible identity system compatible with modern authentication flows.

Phase 2 – Authentication Database Design (Completed)
Models Implemented
1. CustomUser

email (unique)

UUID primary key

is_verified flag

2. EmailVerificationToken

user (ForeignKey)

token (unique)

created_at

expires_at

is_used

Rules:

Tokens expire (10 minutes)

Tokens are single-use

New tokens invalidate old ones

3. UserSession

user

refresh_token

device_name

ip_address

created_at

expires_at

is_revoked

Purpose:

Track active sessions

Enable logout per device

Validate refresh tokens

4. PasswordResetToken

user

token

created_at

expires_at

ip_address

is_used

Phase 3 – Signup Backend Flow (Completed)

This phase implements the full signup + email verification system.

Flow
User Signup
→ Validate request
→ Check duplicate email
→ Hash password
→ Create inactive user (is_verified=False)
→ Generate verification token
→ Send email
→ User clicks link
→ Token validated
→ User activated
Components Implemented
Serializers

RegisterSerializer

EmailVerificationSerializer

Services

user_service → create user

token_service → token lifecycle management

email_service → send verification email

APIs

Signup API

Verify Email API

Key Features

Email-based verification system

Token expiry + single-use enforcement

Clean separation of logic

Production-style flow

Phase 4 – Login + JWT + Session Management (Completed)

This phase implements full authentication and session handling.

Login Flow
User Login
→ Validate request
→ Authenticate user (email + password)
→ Check is_verified
→ Generate JWT tokens
→ Store session in DB
→ Return tokens
Components Implemented
Serializer

LoginSerializer (validation only)

Services
auth_service

authenticate_user(email, password)

jwt_service

generate access and refresh tokens

session_service

create session

revoke session

APIs Implemented
1. Login API

Validates credentials

Returns access + refresh tokens

Creates session

2. Refresh Token API

Accepts refresh token

Validates session

Returns new access token

3. Logout API

Revokes session using refresh token

4. Protected API

Requires valid JWT access token

Uses DRF authentication

System Capabilities

The system now supports:

User signup

Email verification

Secure login

JWT authentication

Session tracking

Token refresh

Logout functionality

Protected endpoints

Folder Structure
login/
│
├── accounts/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── managers.py
│   ├── services/
│   │   ├── user_service.py
│   │   ├── token_service.py
│   │   ├── email_service.py
│   │   ├── auth_service.py
│   │   ├── jwt_service.py
│   │   └── session_service.py
│   └── tests/
│
├── core/
├── manage.py
└── README.md
Architectural Principles

Authentication logic is centralized in accounts

Models store data only

Services handle business logic

Views handle HTTP only

Tokens are single-use and expire

Sessions are tracked for every login

Security Features

Password hashing via Django

Email verification before login

Token expiry enforcement

Single-use tokens

Refresh token session validation

Session revocation (logout)

Optional Improvements (Future Work)

Rate limiting (signup/login)

Async email sending (Celery)

Refresh token rotation

Token blacklisting

Audit logging

Device fingerprinting

Project Status
Phase	Status
Phase 1 – User System	Completed
Phase 2 – DB Design	Completed
Phase 3 – Signup Flow	Completed
Phase 4 – Login + JWT	Completed
Contribution Guidelines

Follow existing architecture

Keep business logic out of views

Design database before APIs

Use service layer for logic

Maintain clear naming

Project Goal

Build a real-world authentication backend that can be reused across multiple projects.

Focus areas:

Security

Scalability

Clean architecture

Maintainability

Reference

This README extends the original project documentation and updates the current system state after completing Phase 3 and Phase 4.

Summary

You now have a complete authentication system:

Signup → Email Verification → Login → JWT → Session → Refresh → Logout

This is production-level backend authentication ready for integration into any web or mobile application.
Authentication System – Updated Project README (Phase 1 → Phase 4)
Introduction

This project implements a production-ready authentication system using Django and Django REST Framework.

The system is designed from scratch instead of relying fully on Django’s default authentication to ensure:

Clean architecture

Strong security practices

Scalability for real-world applications

Architecture Overview

The project follows a strict layered architecture:

APIView (Controller)
    ↓
Serializer (Validation)
    ↓
Service Layer (Business Logic)
    ↓
Manager (Low-level operations)
    ↓
Model (Database)

This separation ensures maintainability and avoids tightly coupled code.

Phase 1 – Custom User System (Completed)
Features Implemented

Custom user model using email as primary identifier

Username removed

UUID as primary key

is_verified flag for email verification

Custom user manager for user and superuser creation

Django admin fully configured

Purpose

Create a flexible identity system compatible with modern authentication flows.

Phase 2 – Authentication Database Design (Completed)
Models Implemented
1. CustomUser

email (unique)

UUID primary key

is_verified flag

2. EmailVerificationToken

user (ForeignKey)

token (unique)

created_at

expires_at

is_used

Rules:

Tokens expire (10 minutes)

Tokens are single-use

New tokens invalidate old ones

3. UserSession

user

refresh_token

device_name

ip_address

created_at

expires_at

is_revoked

Purpose:

Track active sessions

Enable logout per device

Validate refresh tokens

4. PasswordResetToken

user

token

created_at

expires_at

ip_address

is_used

Phase 3 – Signup Backend Flow (Completed)

This phase implements the full signup + email verification system.

Flow
User Signup
→ Validate request
→ Check duplicate email
→ Hash password
→ Create inactive user (is_verified=False)
→ Generate verification token
→ Send email
→ User clicks link
→ Token validated
→ User activated
Components Implemented
Serializers

RegisterSerializer

EmailVerificationSerializer

Services

user_service → create user

token_service → token lifecycle management

email_service → send verification email

APIs

Signup API

Verify Email API

Key Features

Email-based verification system

Token expiry + single-use enforcement

Clean separation of logic

Production-style flow

Phase 4 – Login + JWT + Session Management (Completed)

This phase implements full authentication and session handling.

Login Flow
User Login
→ Validate request
→ Authenticate user (email + password)
→ Check is_verified
→ Generate JWT tokens
→ Store session in DB
→ Return tokens
Components Implemented
Serializer

LoginSerializer (validation only)

Services
auth_service

authenticate_user(email, password)

jwt_service

generate access and refresh tokens

session_service

create session

revoke session

APIs Implemented
1. Login API

Validates credentials

Returns access + refresh tokens

Creates session

2. Refresh Token API

Accepts refresh token

Validates session

Returns new access token

3. Logout API

Revokes session using refresh token

4. Protected API

Requires valid JWT access token

Uses DRF authentication

System Capabilities

The system now supports:

User signup

Email verification

Secure login

JWT authentication

Session tracking

Token refresh

Logout functionality

Protected endpoints

Folder Structure
login/
│
├── accounts/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── managers.py
│   ├── services/
│   │   ├── user_service.py
│   │   ├── token_service.py
│   │   ├── email_service.py
│   │   ├── auth_service.py
│   │   ├── jwt_service.py
│   │   └── session_service.py
│   └── tests/
│
├── core/
├── manage.py
└── README.md
Architectural Principles

Authentication logic is centralized in accounts

Models store data only

Services handle business logic

Views handle HTTP only

Tokens are single-use and expire

Sessions are tracked for every login

Security Features

Password hashing via Django

Email verification before login

Token expiry enforcement

Single-use tokens

Refresh token session validation

Session revocation (logout)

Optional Improvements (Future Work)

Rate limiting (signup/login)

Async email sending (Celery)

Refresh token rotation

Token blacklisting

Audit logging

Device fingerprinting

Project Status
Phase	Status
Phase 1 – User System	Completed
Phase 2 – DB Design	Completed
Phase 3 – Signup Flow	Completed
Phase 4 – Login + JWT	Completed
Contribution Guidelines

Follow existing architecture

Keep business logic out of views

Design database before APIs

Use service layer for logic

Maintain clear naming

Project Goal

Build a real-world authentication backend that can be reused across multiple projects.

Focus areas:

Security

Scalability

Clean architecture

Maintainability

Reference

This README extends the original project documentation and updates the current system state after completing Phase 3 and Phase 4.

Summary

You now have a complete authentication system:

Signup → Email Verification → Login → JWT → Session → Refresh → Logout

This is production-level backend authentication ready for integration into any web or mobile application.