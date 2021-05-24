URL = "http://localhost:8000/api/token/"

user = {
      "email": "jhabar@msrit.edu",
      "password": "Jhabar@123"
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

