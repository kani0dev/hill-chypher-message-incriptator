# Hill Cipher Encryption/Decryption API

This project provides a simple REST API for encrypting and decrypting messages using the Hill Cipher algorithm. It includes a Python backend (FastAPI) and a React frontend.

## Folder Structure

```
.
├── controller -> Manage endpoints and service
│   ├── __init__.py
│   ├── main.py
│   ├── Dockerfile
│   └── requirements.txt
│   └── service/
│       ├── cipher_utils.py
│       └── constants.py
└── view -> Simple React frontend (for reference, not required for backend)
    ├── public/
    ├── src/
    ├── package.json
    └── ... (standard React app structure)
```

## Backend (Python/FastAPI)

### Running with Docker

1. **Build the Docker image**:
   ```bash
   docker build -t hill-cipher-backend ./controller
   ```

2. **Run the container**:
   ```bash
   docker run -p 8000:8000 hill-cipher-backend
   ```

### Dockerfile Explained (step by step)

The Dockerfile in the `controller` directory:

```dockerfile
FROM python:3.12-slim          # Use a lightweight Python 3.12 image
WORKDIR /app                   # Set working directory inside the container

COPY requirements.txt .        # Copy Python dependencies
RUN pip install --no-cache-dir -r requirements.txt fastapi[standard]  # Install dependencies and FastAPI with standard extras

COPY . .                       # Copy the rest of the application code

EXPOSE 8000                    # Expose port 8000 for the API

CMD ["fastapi", "run", "--port", "8000"]  # Start the FastAPI server
```

### Running without Docker (Development)

1. Install dependencies:
   ```bash
   pip install -r controller/requirements.txt
   ```

2. Start the server:
   ```bash
   cd controller
   fastapi run --port 8000
   ```

### API Endpoints

- `POST /encrypt`: Encrypt a message using the Hill Cipher.
- `POST /decrypt`: Decrypt a message using the Hill Cipher.

Both endpoints expect a JSON body with a `message` field.

Example request:
```json
{
  "message": "hello"
}
```

## Frontend (React)

The frontend is located in the `view` directory. It provides a simple interface to interact with the API.

### Running the Frontend

1. Navigate to the view directory:
   ```bash
   cd view
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

   (Assuming the project uses Vite, as indicated by the presence of `vite` in dependencies. If not, adjust the command accordingly.)

### Note
The frontend is configured to communicate with the backend at `http://localhost:8000`. Ensure the backend is running before using the frontend.
## Security Note

This implementation is for educational purposes only. The Hill Cipher is not secure by modern standards and should not be used for protecting sensitive information.
