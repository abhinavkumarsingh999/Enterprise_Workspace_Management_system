# Logger Documentation

## Overview

The project uses Python's built-in logging module to record application events.

Logging helps developers:

- Track application execution
- Debug errors
- Monitor system activity
- Record warnings
- Maintain execution history

---

## Log Levels

### INFO

Used for normal application events.

Example

```
Application Started
```

---

### WARNING

Used when something unexpected happens but the application continues.

Example

```
Configuration file not found.
```

---

### ERROR

Used when an operation fails.

Example

```
Database connection failed.
```

---

### CRITICAL

Used for severe errors that may stop the application.

Example

```
Application crashed.
```

---

## Log File

Logs are stored inside

```
logs/
```

Example

```
application.log
```

---

## Advantages

- Easier debugging
- Better monitoring
- Improved troubleshooting
- Professional software maintenance