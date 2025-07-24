import requests # type: ignore

API_URL = "http://localhost:8000"

demo_users = [
    {"name": "Mario Rossi", "email": "mario.rossi@example.com"},
    {"name": "Lucia Bianchi", "email": "lucia.bianchi@example.com"},
    {"name": "Alessandro Verdi", "email": "alessandro.verdi@example.com"}
]

for user in demo_users:
    response = requests.post(f"{API_URL}/add_user", json=user)
    print(f"Inserimento {user['name']}: {response.status_code} - {response.text}")