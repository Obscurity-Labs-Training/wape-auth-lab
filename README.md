# wape-auth-lab

This repository demonstrates two types of authentication using **FastAPI**:
- **Basic Authentication**
- **JWT (Bearer Token) Authentication**

Both authentication mechanisms are implemented using FastAPI, and you can easily test the authentication via **curl**, **Postman**, or **Swagger UI**.

## Getting Started

### Prerequisites
- **Docker** and **Docker Compose** must be installed on your system.

### Setup and Run the Application

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Obscurity-Labs-Training/wape-auth-lab.git
   cd wape-auth-lab
   ```

2. **Build the Docker image**:
   ```bash
   docker compose build
   ```

3. **Run the application**:
   ```bash
   docker compose up
   ```

The application will be available at `http://localhost:8000`.

You can test the routes using **curl**, **Postman**, or by visiting **Swagger UI** at `http://localhost:8000/docs`.

---

## API Routes

- **/basic-auth**:
  - Protected by **Basic Authentication**.
  - Requires a username (`admin`) and password (`password`).
  
- **/login**:
  - Used to **generate a JWT token**.
  - Requires Basic Authentication (username: `admin`, password: `password`).
  
- **/jwt-auth**:
  - Protected by **JWT Authentication**.
  - Requires the **Bearer token** received from the `/login` route.

---

## Labs

### **Lab 1: Basic Authentication**

#### Objective:
In this lab, you will authenticate using **Basic Authentication** to access a protected route.

#### Instructions:

1. **Make a request to the `/basic-auth` route** using **Basic Authentication** with the following credentials:
   - **Username**: `admin`
   - **Password**: `password`

2. You can test this using **curl**:
   ```bash
   curl -u admin:password http://localhost:8000/basic-auth
   ```

3. If authentication is successful, the server will respond with:
   ```json
   {
     "message": "Successfully authenticated using Basic Auth!"
   }
   ```

4. **Test invalid credentials**:
   - Try using incorrect credentials (e.g., `admin:wrongpassword`).
   - The server should respond with a `401 Unauthorized` status.

#### Goal:
- Understand how to authenticate users using Basic Authentication and learn about how credentials are passed via HTTP headers.

---

### **Lab 2: JWT Authentication**

#### Objective:
In this lab, you will generate a **JWT token** and use it to authenticate and access a protected route.

#### Instructions:

1. **Generate a JWT token**:
   - Make a POST request to the `/login` route using **Basic Authentication** with the credentials:
     - **Username**: `admin`
     - **Password**: `password`

2. You can test this using **curl**:
   ```bash
   curl -u admin:password -X POST http://localhost:8000/login
   ```

3. The server will respond with a JWT token:
   ```json
   {
     "token": "<your-jwt-token>"
   }
   ```

4. **Use the JWT token to access the `/jwt-auth` route**:
   - Send a request to `/jwt-auth` with the token in the `Authorization` header.
   - The token must be sent in the format `Bearer <your-jwt-token>`.

   Example using **curl**:
   ```bash
   curl -H "Authorization: Bearer <your-jwt-token>" http://localhost:8000/jwt-auth
   ```

5. If authentication is successful, the server will respond with:
   ```json
   {
     "message": "Successfully authenticated using JWT Auth!"
   }
   ```

6. **Test invalid or expired tokens**:
   - Modify the token or send an empty token to see how the server responds.
   - You should receive a `403 Forbidden` status with an appropriate error message.

#### Goal:
- Understand how **JWT authentication** works, how to generate and use tokens for authentication, and how tokens are validated on the server.

---

## Conclusion

This demo application covers both **Basic Authentication** and **JWT Authentication** in a simple FastAPI project. You can extend this further to support more complex authentication workflows, add role-based access control, or integrate with third-party OAuth providers.

