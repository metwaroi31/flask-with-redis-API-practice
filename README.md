# flask-with-redis-API-practice

# run the app

- To run the app. Use commane `docker-compose up`

# request

- POST /sensor 

example request:


{
  "id": "36d5658a-6908-479e-887e-a949ec199272",
    "readings": [{
      "timestamp": "2021-09-29T16:08:15+01:00",
      "count": 2
}, {
      "timestamp": "2021-09-29T16:09:15+01:00",
"count": 15 }
] }


- GET /sensor/<uuid>?timestamp=True

This will return latest timestamp

- GET /sensor/<uuid>?count=True

This will return cumulative_count