# Simple FastAPI Blog

This is a FastAPI project created as part of the Bitfumes YouTube tutorial series. The project demonstrates how to build a simple blog API using FastAPI.

## Getting Started

### Prerequisites

- Python 3.8+
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/) (for running the server)

### Setup Instructions

1. **Clone the repository**

   ```bash
   git clone <your-repo-url>
   cd fast-api-blog-tutorial
   ```

2. **Create and activate a virtual environment**

   ```bash
   python3 -m venv fastapi-env
   source fastapi-env/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install fastapi uvicorn
   ```

4. **Run the FastAPI server**
   ```bash
   uvicorn main:app --reload
   ```
   - The API will be available at: http://127.0.0.1:8000
   - Interactive API docs: http://127.0.0.1:8000/docs

## About

This project is based on the Bitfumes YouTube tutorial for building a simple blog API with FastAPI.

- YouTube Channel: [Bitfumes](https://www.youtube.com/bitfumes)

---

Feel free to contribute or use this as a starting point for your own FastAPI projects!
