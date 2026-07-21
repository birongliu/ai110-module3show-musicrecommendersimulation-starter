"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


# At least three distinct user preference profiles to simulate different tastes.
USER_PROFILES = {
    "High-Energy Pop": {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.9,
        "likes_acoustic": False,
    },
    "Chill Lofi": {
        "favorite_genre": "lofi",
        "favorite_mood": "chill",
        "target_energy": 0.3,
        "likes_acoustic": True,
    },
    "Deep Intense Rock": {
        "favorite_genre": "rock",
        "favorite_mood": "intense",
        "target_energy": 0.85,
        "likes_acoustic": False,
    },
}


def print_recommendations(profile_name: str, user_prefs: dict, songs: list) -> None:
    recommendations = recommend_songs(user_prefs, songs, k=5)

    header = f"TOP RECOMMENDATIONS — {profile_name}"
    width = 60
    print()
    print("=" * width)
    print(header.center(width))
    print("=" * width)

    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        reasons = explanation.split("; ")
        print()
        print(f"{rank}. {song['title']} — {song['artist']}")
        print(f"   Score: {score:.2f} / 8.00")
        print("   Reasons:")
        for reason in reasons:
            print(f"     • {reason}")

    print()
    print("=" * width)


def main() -> None:
    songs = load_songs("data/songs.csv")

    for profile_name, user_prefs in USER_PROFILES.items():
        print_recommendations(profile_name, user_prefs, songs)


if __name__ == "__main__":
    main()
