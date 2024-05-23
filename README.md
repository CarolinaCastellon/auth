# Microservicio de autenticación

## Descripción

Este microservicio se encarga de gestionar la autenticación de los usuarios.

## Configuración

### Iniciar proyecto

Inicializar el entorno virtual.

```bash
python3 -m venv .venv
```

Activar el entorno virtual en MacOS/Linux:

```bash
$ source .venv/bin/activate
```

Windows:

```PowerShell
PS C:\> \.venv\Scripts\Activate.ps1
```

Instalar las dependencias.

```bash
pip install -r requirements.txt
```

Iniciar el servidor de desarrollo.

```bash
python app.py
```

### Variables de entorno

- `DB_USER`: Usuario de la base de datos. **Requerido**
- `DB_PASS`: Contraseña de la base de datos. **Requerido**
- `DB_HOST`: Host de la base de datos. **Requerido**
- `DB_PORT`: Puerto de la base de datos. **Requerido**
- `DB_NAME`: Nombre de la base de datos. **Requerido**
- `PORT`: Puerto en el que se ejecutará el servidor. **Requerido**
- `JWT_SECRET_KEY`: Clave secreta para firmar los tokens JWT. **Requerido**
- `PORT`: Puerto en el que se ejecutará el servidor de desarrollo. **Requerido**

## Endpoints

### `POST /login`

Inicia sesión en la aplicación.

request body:

```json
{
  "email": "example@example.com",
  "password": "password123"
}
```

### `POST /register`

Registra un nuevo usuario.

request body:

```json
{
  "email": "example@example.com",
  "password": "password123"
}
```
