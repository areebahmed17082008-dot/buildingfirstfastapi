# Building First API

A simple Flask API with two endpoints:

- `GET /get-user/<user_id>`: returns a sample user object
- `POST /create-user`: accepts JSON input and returns it back

## Setup

1. Create a virtual environment (optional but recommended):
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the server:
   ```bash
   python3 main.py
   ```

## Example requests

```bash
curl http://127.0.0.1:5000/get-user/42?extra=yes
```

```bash
curl -X POST http://127.0.0.1:5000/create-user \
  -H "Content-Type: application/json" \
  -d '{"name":"Alice"}'
```

## Notes

- Invalid JSON in `POST /create-user` returns a `400` response.
- The app runs in debug mode during local development.