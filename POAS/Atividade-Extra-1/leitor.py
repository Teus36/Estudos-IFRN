import requests

with open("./20250702_Pedidos_csv_2025.csv", "rb") as f:
    response = requests.post("http://localhost:8000/upload-csv/", files={"file": f})

print("Status:", response.status_code)
print("Texto bruto:", response.text)