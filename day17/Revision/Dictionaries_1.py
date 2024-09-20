# operation = int(input("Enter your choice for 1.Add movie\n2.Vote\n3.Remove movie\n4.Display votes\n5.Top movie"))
di = {}
def add_movie():
    choice = 'yes'
    while True:
        if choice=='yes':
            movies = input("Enter the movie name:")
            di[movies] = 0
        choice = input("do you wnat to add more movies or not? yes or no")
        if choice=='no':
            break
    return di


def update_vote():
    vote = input("Hey! vote for the movie yes or no")
    if vote == 'yes':
        vote_movie = input("Which movie you want to vote for:")
        di[vote_movie] += 1
        return di
    elif vote == 'no':
        return di

print(add_movie())
print(update_vote())


