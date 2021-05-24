{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYyMTk1Njg5NywianRpIjoiNDQ4NzM3OGNiYWU0NGQ0YThjZGU4ZmY2MDVhNjRmNjUiLCJ1c2VyX2lkIjozfQ.v93j6Q0SDqmPuJFraN_SshH46dGktuDhxuBK8embUBw",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjIxOTU2ODk3LCJqdGkiOiJiNDYwMWZkNDZlMzE0ZWY0OThjYjFiYTU3MjY1NTQzYiIsInVzZXJfaWQiOjN9.j9BpR1wEt5MrfaZ_ev7NILzvg99k0wz06QsaaFBdEkM"
}

URL = "http://ec2-18-224-181-83.us-east-2.compute.amazonaws.com/users/create/"

URL = "http://localhost:8000/api/token/refresh/"

user = {
      "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYyMTk1Njg5NywianRpIjoiNDQ4NzM3OGNiYWU0NGQ0YThjZGU4ZmY2MDVhNjRmNjUiLCJ1c2VyX2lkIjozfQ.v93j6Q0SDqmPuJFraN_SshH46dGktuDhxuBK8embUBw",
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

