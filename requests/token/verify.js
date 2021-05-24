eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90e…iOjN9.vgMqgp-WOCzck4y47ZHNj1fE-0OOH-w2iZOVBvfYOYQ

URL = "http://localhost:8000/api/token/verify/"

user = {
      "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjIxOTU3MTcxLCJqdGkiOiJjZWUyMzZjZjU2ZmU0YjRiOGNlNzg3M2RjMmRkN2Y3YSIsInVzZXJfaWQiOjN9.sqKcBO1JhuB-1UBDfAOau7Qc7jivD_ziojzFvDiYZB8"
}

let options = {
        method: 'POST',
        headers: {
                'Content-Type': 'application/json',
        },
        body: JSON.stringify(user),
 }

fetch(URL, options).then(res => {
        return res.json();
}).then(res => {
        console.log(res);
});

