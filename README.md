# 📡 IoT Telemetry API

A simple RESTful API built with **FastAPI** for receiving and managing IoT telemetry data.

This project demonstrates how to build a clean backend API that:

- Accepts telemetry data in JSON format
- Validates incoming data
- Stores records in memory
- Exposes multiple REST endpoints
- Provides automatic interactive documentation

---

## 🚀 Features

- ✅ `GET /` – API status check
- ✅ `GET /health` – Health monitoring endpoint
- ✅ `POST /telemetry` – Submit IoT telemetry data
- ✅ `GET /telemetry` – Retrieve stored telemetry records
- ✅ Input validation using Pydantic
- ✅ In-memory data storage
- ✅ Automatic Swagger documentation (`/docs`)

---

## 🛠 Tech Stack

- Python 3.10+
- FastAPI
- Uvicorn
- Pydantic

---

## 📂 Project Structure

```
iot-telemetry-api/
│
├── main.py
├── requirements.txt
└── README.md
```

---

## 📦 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/1khaled-ctr/iot-telemetry-api.git
cd iot-telemetry-api
```

Replace `1khaled-ctr` with your actual GitHub username.

---

### 2️⃣ Install Dependencies

#### Windows

```bash
py -m pip install -r requirements.txt
```

#### macOS / Linux

```bash
python3 -m pip install -r requirements.txt
```

---

## ▶ Running the Server

#### Windows

```bash
py -m uvicorn main:app --reload
```

#### macOS / Linux

```bash
python3 -m uvicorn main:app --reload
```

The API will start at:

```
http://127.0.0.1:8000
```

Interactive API documentation:

```
http://127.0.0.1:8000/docs
```

---

## 📥 API Endpoints

### 🔹 GET /

Returns API status.

Example Response:

```json
{
  "message": "IoT Telemetry API is running",
  "status": "ok"
}
```

---

### 🔹 GET /health

Simple health check endpoint.

Example Response:

```json
{
  "ok": true
}
```

---

### 🔹 POST /telemetry

Submit telemetry data in JSON format.

Example Request:

```json
{
  "device_id": "sensor-001",
  "temperature": 22.4,
  "humidity": 55.1,
  "timestamp": "2026-03-01T10:30:00"
}
```

Example Response:

```json
{
  "ok": true,
  "stored_records": 1,
  "data": {
    "device_id": "sensor-001",
    "temperature": 22.4,
    "humidity": 55.1,
    "timestamp": "2026-03-01T10:30:00"
  }
}
```

---

### 🔹 GET /telemetry

Retrieve stored telemetry records.

Query Parameters:

- `limit` (optional, default = 50) → Number of records to return

Example:

```
GET /telemetry?limit=10
```

---

## 🧠 Data Validation Rules

| Field        | Rule |
|-------------|------|
| device_id   | 1–64 characters |
| temperature | -50 to 150 |
| humidity    | 0 to 100 |
| timestamp   | ISO 8601 datetime format |

Invalid data will automatically return a 422 validation error.

---

## ⚠️ Important Notes

- Telemetry data is stored **in memory only**.
- Restarting the server will erase stored data.
- This project is intended for learning and demonstration purposes.

For production usage, consider integrating:

- SQLite
- PostgreSQL
- Authentication
- Persistent storage
- Logging and monitoring

---

## 📌 Future Improvements

- Add database persistence
- Add authentication (API key or JWT)
- Add Docker support
- Deploy to cloud (Render, Railway, AWS)
- Add structured logging
- Add unit tests

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author
1khaled-ctrl
