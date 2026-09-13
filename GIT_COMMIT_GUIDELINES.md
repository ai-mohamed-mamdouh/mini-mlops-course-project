# Git Commit Guidelines

This document defines the commit convention that will be followed in all projects.

The goal is to keep the Git history clean, readable, and easy to understand.

---

# Commit Message Format

All commits should follow this structure:

```text
<type>: <description>
```

Example:

```text
feat: add user authentication feature
```

---

# Commit Types

## 1. feat — Add a New Feature

Used when adding a new functionality or capability to the project.

Examples:

```text
feat: add ONNX model loader

feat: add user authentication system

feat: implement payment integration
```

---

## 2. fix — Fix a Bug or Issue

Used when correcting an error or unexpected behavior.

Examples:

```text
fix: fix incorrect model prediction output

fix: handle missing input validation

fix: resolve database connection issue
```

---

## 3. refactor — Improve Code Structure

Used when changing the internal structure of the code without changing its behavior.

Examples:

```text
refactor: simplify preprocessing pipeline

refactor: reorganize project modules

refactor: improve model loading logic
```

---

## 4. test — Add or Modify Tests

Used when adding tests or improving test coverage.

Examples:

```text
test: add prediction API tests

test: add unit tests for preprocessing functions

test: improve model validation tests
```

---

## 5. docs — Update Documentation

Used for changes related to documentation.

Examples:

```text
docs: update project README

docs: add API usage examples

docs: document installation steps
```

---

## 6. chore — Project Maintenance

Used for configuration, setup, dependencies, or administrative tasks.

Examples:

```text
chore: initialize project structure

chore: update dependencies

chore: add environment configuration

chore: containerize ML API
```

---

## 7. ci — Continuous Integration Changes

Used for CI/CD pipeline changes.

Examples:

```text
ci: add GitHub Actions pipeline

ci: automate testing workflow

ci: add Docker build workflow
```

---

# Example Project Commit History

A typical project workflow:

```text
chore: initialize project structure

feat: add ONNX model loader

feat: add input preprocessing pipeline

feat: add output postprocessing pipeline

feat: implement end-to-end inference pipeline

feat: add API schemas

feat: expose model prediction API

chore: containerize ml api

test: add prediction API tests

ci: add GitHub Actions pipeline
```

---

# Commit Best Practices

## 1. Keep commits small and focused

A commit should represent one logical change.

Good:

```text
feat: add model prediction endpoint
```

Bad:

```text
update everything
```

---

## 2. Write commits in the imperative form

Use:

```text
add feature
fix bug
update documentation
```

Avoid:

```text
added feature
fixed bug
updated documentation
```

---

## 3. Commit after completing a meaningful unit

Do not commit every small change.

Commit when you finish a complete task:

Example:

```
Preprocessing module completed
        ↓
commit
```

```
FastAPI endpoint completed
        ↓
commit
```

---

## 4. Keep the Git history readable

A clean history should explain the project evolution:

```
Project setup
      ↓
Model integration
      ↓
API development
      ↓
Testing
      ↓
Deployment
      ↓
Automation
```

---

Following this convention makes projects easier to maintain, collaborate on, and review professionally.