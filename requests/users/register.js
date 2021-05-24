URL = "http://ec2-18-224-181-83.us-east-2.compute.amazonaws.com/users/create/"

URL = "http://localhost:8000/users/create/"

user = {
      "username": "jhabarsinghbhat12i",
      "first_name": "jhabar",
      "last_name": "singh",
      "date_of_birth": "2021-05-08",
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
