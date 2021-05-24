url = "http://ec2-18-224-181-83.us-east-2.compute.amazonaws.com/users/"

fetch(url).then(res => res.json()).then(res => console.log(res))

