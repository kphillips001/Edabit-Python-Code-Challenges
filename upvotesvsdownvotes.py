# Given a dictionary containing counts of both upvotes and downvotes, return what vote count should be displayed. This is calculated by subtracting the number of downvotes from upvotes.

# Notes
# You can expect only positive integers for vote counts.
def get_vote_count(votes):
	return (votes.get('upvotes') - votes.get('downvotes'))