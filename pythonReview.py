def create_youtube_video (title, description):
	hashtags = set()
	for i in range(5):
		hashtags.add(input("Enter hashtag: "))
	video= {"title": title, "desription": description, "likes": 0, "dislikes" : 0, "comments":{}, "hashtag":hashtags}
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
youtubevideo2= create_youtube_video("no","ok")
hashtags1=youtubevideo['hashtag']
hashtags2= youtubevideo2['hashtag']
commonhashtags=0
for i in hashtags1:  
	if i in hashtags2:
		commonhashtags += 1
		
print(commonhashtags)
percentage= (commonhashtags/max(len(hashtags1),len(hashtags2)))*100
print(str(percentage) + '%')
like(youtubevideo)
dislike(youtubevideo)
add_comment(youtubevideo,"zena","hi")
for i in range(495):
	like(youtubevideo)
print(youtubevideo)
print(youtubevideo2)