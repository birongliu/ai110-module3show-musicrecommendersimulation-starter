from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return the top k songs scored against the user's preferences."""
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Return a human-readable reason why the song was recommended to the user."""
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    songs = []
    with open(csv_path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            song = {
                'id': int(row['id']),
                'title': row['title'],
                'artist': row['artist'],
                'genre': row['genre'],
                'mood': row['mood'],
                'energy': float(row['energy']),
                'tempo_bpm': float(row['tempo_bpm']),
                'valence': float(row['valence']),
                'danceability': float(row['danceability']),
                'acousticness': float(row['acousticness']),
            }
            songs.append(song)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    # Weighted point system from the Algorithm Recipe (README). Max score = 8.0.
    score = 0.0
    reasons: List[str] = []

    # Genre match: +3.0 (categorical, no partial credit — earns the most)
    if song['genre'] == user_prefs['favorite_genre']:
        score += 3.0
        reasons.append(f"Genre match ({song['genre']})")

    # Mood match: +2.0 (moods overlap, so a miss is more forgivable than genre)
    if song['mood'] == user_prefs['favorite_mood']:
        score += 2.0
        reasons.append(f"Mood match ({song['mood']})")

    # Energy fit: +2.0 max, scaled by closeness to target energy
    energy_points = 2.0 * (1 - abs(song['energy'] - user_prefs['target_energy']))
    if energy_points > 0:
        score += energy_points
        reasons.append(f"Energy fit ({energy_points:.2f})")

    # Acoustic preference: +1.0 tiebreaker
    if user_prefs['likes_acoustic'] and song['acousticness'] >= 0.6:
        score += 1.0
        reasons.append("Acoustic preference")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    # Score every song, sort by score descending, return the top k (Algorithm Recipe).
    scored = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "; ".join(reasons) if reasons else "No matching preferences"
        scored.append((song, score, explanation))

    scored.sort(key=lambda item: item[1], reverse=True)
    return scored[:k]
