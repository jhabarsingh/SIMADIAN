categories = [
	"Action & Adventure",
	"Arts, Film & Photography",
	"Biographies, Diaries & True Accounts",
	"Children's & Young Adult",
	"Crafts, Hobbies & Home",
	"Crime, Thriller & Mystery",
	"Science Fiction & Fantasy",
	"Health, Family & Personal Development",
	"History",
	"Literature & Fiction",
	"Religion & Spirituality",
	"Romance",
	"School Books",
	"Textbooks & Study Guides"
]


for(let i = 0; i<categories.length; i++) {
        fetch("http://localhost:8000/items/category/create/", {
                method: "POST",
		headers: {
       	 		'Content-Type': 'application/json'
      		},
                body: JSON.stringify({
                        category: categories[i],
                })
        }).then(res => console.log(res))
        .catch(err => console.log(err));
}

