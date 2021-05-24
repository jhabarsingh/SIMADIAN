URL = "http://ec2-18-224-181-83.us-east-2.compute.amazonaws.com/api/token/"

user = {
      "email": "jhabar@msrit.edu",
      "password": "labsana@123"
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
