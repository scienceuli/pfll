from pymongo import MongoClient

client = MongoClient()

db = client.pymongo_test

posts = db.posts
post_data = {
    "title": "Ulis erster Post",
    "content": "Ich hoffe, es klappt alles.",
    "author": "Uli",
}
result = posts.insert_one(post_data)
print("One post: {0}".format(result.inserted_id))


ulis_post = posts.find_one({"author": "Uli"})
print(ulis_post)

# index test
# 

db.categories.insertMany( [
   { _id: "Index", path: null },
   { _id: "Programming", path: ",Books," },
   { _id: "Databases", path: ",Books,Programming," },
   { _id: "Languages", path: ",Books,Programming," },
   { _id: "MongoDB", path: ",Books,Programming,Databases," },
   { _id: "dbm", path: ",Books,Programming,Databases," }
] )
