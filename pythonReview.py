def create_youtube_video (title, description):
	video= {"title": title, "description": description, "likes": 0, "dislikes" : 0, "comments":{}}
	return video 

def like(video):
	if "likes" in video:
		li=video["likes"]
		video["likes"]= li+1 
	return video

def dislike(video):
	if "dislikes" in video:
		disli= video["dislikes"]
		video["dislikes"]= disli+1
	return video
def add_comment(video, username, comment_text):
	video["comments"][username]=comment_text
	return video

youtubevideo=create_youtube_video("yes","ok")
like(youtubevideo)
dislike(youtubevideo)
add_comment(youtubevideo,"zena","hi")
print(youtubevideo)
for i in range(495):
	like(youtubevideo)
print(youtubevideo)