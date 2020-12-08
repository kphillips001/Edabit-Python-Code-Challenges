# You have two lists. One shows the names of the people, while the other shows their occupation. Your task is to make a dictionary displaying each person to their respective occupations.

def assign_person_to_job(pl, jl):
	return {pl[i] : jl[i] for i in range(len(pl))}