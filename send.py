import requests

headers = {}
headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM1NTExNzIzLCJpYXQiOjE2MzU1MTA1OTUsImp0aSI6IjUzMTE0NzA5OGRmMTQ0NTA4NTcxN2M2ZTE1OGE2MDUzIiwidXNlcl9pZCI6MX0.wrqrZ3sj9MVZpU_R-_euOTe7uZPbrW0unfo8dS4frXo'

r = requests.get('http://127.0.0.1:8000/paradigms', headers=headers)

print(r.text)