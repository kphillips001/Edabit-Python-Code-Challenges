# After an amazing performance, the crowd goes wild! People clap enthusiastically and most claps overlap with each other to create one homogeneous sound.

# An overlapped clap is a clap which starts but doesn't finish, as in "ClaClap" (the first clap is cut short and there are overall 2 claps).

# Given a string of what the overlapping claps sounded like, return how many claps were made in total.

def count_claps(txt):
	return txt.count("C")