# Technology Stack

## Runtime Environment
* **Language Environment:** Python 3.11+
* **Framework Layer:** FastAPI (Asynchronous engine routing)
* **Dependency Toolset:** `pipreqs` for pinpointing accurate import footprints.

## Engineering Rules
1. All file interactions and system calls must rely on asynchronous, non-blocking wrappers.
2. Utilize core primitive libraries (`hashlib`, `hmac`) over external third-party dependencies wherever mathematically viable.