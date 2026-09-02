# Collaborative Filtering Recommendation System

ratings = {
    "User1": {
        "MovieA": 5,
        "MovieB": 4,
        "MovieC": 1
    },

    "User2": {
        "MovieA": 5,
        "MovieB": 4,
        "MovieD": 5
    },

    "User3": {
        "MovieA": 1,
        "MovieC": 5,
        "MovieD": 4
    }
}

user = input("Enter user name (User1/User2/User3): ")

if user not in ratings:

    print("User not found.")

else:

    print("\nYour Ratings:")
    print(ratings[user])

    recommendations = []

    # Find movies highly rated by other users
    for other_user in ratings:

        if other_user == user:
            continue

        for movie in ratings[other_user]:

            if movie not in ratings[user]:

                if ratings[other_user][movie] >= 4:

                    if movie not in recommendations:
                        recommendations.append(movie)

    print("\nRecommended Movies:")

    if len(recommendations) == 0:
        print("No recommendations available.")

    else:
        for movie in recommendations:
            print(movie)
