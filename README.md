# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.
going with content based filtering recommandation because

Real streaming platforms like Spotify and YouTube use two main strategies to predict what you'll love: collaborative filtering (finding users with similar taste and recommending what they enjoyed) and content based filtering (analyzing song attributes like energy, tempo, and mood to find similar songs to ones you like). Most platforms use a hybrid approach: collaborative filtering discovers serendipitous picks, while content-based filtering handles new songs and avoids echo chambers. will be priortizing content based filtering


Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
    id, title, artist, genre, mood, energy, tempo_bpm, valence, danceability, acousticness
- What information does your `UserProfile` store
  - id, username, song, favorite_genre, favorite_mood, target_energy, likes_acoustic
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

### Algorithm Recipe

Each song is scored against the `UserProfile` using a weighted point system. Signals
that define taste most rigidly are worth the most points; fuzzy or nice-to-have
signals are worth less.

| Signal | Points | Rule |
| --- | --- | --- |
| Genre match | **+3.0** | `song.genre == user.favorite_genre` (categorical — no partial credit, so it earns the most) |
| Mood match | **+2.0** | `song.mood == user.favorite_mood` (moods overlap emotionally, so a miss is more forgivable than genre) |
| Energy fit | **+2.0 max** | scaled: `2.0 * (1 - abs(song.energy - user.target_energy))` — near matches earn partial credit |
| Acoustic preference | **+1.0** | `user.likes_acoustic and song.acousticness >= 0.6` (tiebreaker) |

**Maximum score = 8.0.** A Mood match is worth ⅔ of a Genre match (2.0 vs 3.0) because
genre is a hard, categorical boundary while moods overlap. Keeping them close (3:2, not
3:1) lets a strong mood + energy match (2.0 + 2.0 = 4.0) outrank a genre-only match (3.0),
which is usually the more pleasing result.

**Choosing recommendations:** score every song, sort by score descending, and return the
top `k`. Each recommendation carries a short list of the reasons that earned it points,
used to explain the pick to the user.

You can include a simple diagram or bullet list if helpful.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```

============================================================
                    TOP RECOMMENDATIONS                     
============================================================

1. Sunrise City — Neon Echo
   Score: 6.96 / 8.00
   Reasons:
     • Genre match (pop)
     • Mood match (happy)
     • Energy fit (1.96)

2. Gym Hero — Max Pulse
   Score: 4.74 / 8.00
   Reasons:
     • Genre match (pop)
     • Energy fit (1.74)

3. Rooftop Lights — Indigo Parade
   Score: 3.92 / 8.00
   Reasons:
     • Mood match (happy)
     • Energy fit (1.92)

4. Night Drive Loop — Neon Echo
   Score: 1.90 / 8.00
   Reasons:
     • Energy fit (1.90)

5. Crown Jewel — King Vibe
   Score: 1.84 / 8.00
   Reasons:
     • Energy fit (1.84)

============================================================
(ai110-module3show-musicrecommendersimulation-starter) 11:50 PM ai110-module3show-musicrecommendersimulation-starter (main) > 
(ai110-module3show-musicrecommendersimulation-starter) 11:50 PM ai110-module3show-musicrecommendersimulation-starter (main) > python src/main.py

============================================================
           TOP RECOMMENDATIONS — High-Energy Pop            
============================================================

1. Sunrise City — Neon Echo
   Score: 6.84 / 8.00
   Reasons:
     • Genre match (pop)
     • Mood match (happy)
     • Energy fit (1.84)

2. Gym Hero — Max Pulse
   Score: 4.94 / 8.00
   Reasons:
     • Genre match (pop)
     • Energy fit (1.94)

3. Rooftop Lights — Indigo Parade
   Score: 3.72 / 8.00
   Reasons:
     • Mood match (happy)
     • Energy fit (1.72)

4. Storm Runner — Voltline
   Score: 1.98 / 8.00
   Reasons:
     • Energy fit (1.98)

5. Crown Jewel — King Vibe
   Score: 1.96 / 8.00
   Reasons:
     • Energy fit (1.96)

============================================================

============================================================
              TOP RECOMMENDATIONS — Chill Lofi              
============================================================

1. Library Rain — Paper Lanterns
   Score: 7.90 / 8.00
   Reasons:
     • Genre match (lofi)
     • Mood match (chill)
     • Energy fit (1.90)
     • Acoustic preference

2. Midnight Coding — LoRoom
   Score: 7.76 / 8.00
   Reasons:
     • Genre match (lofi)
     • Mood match (chill)
     • Energy fit (1.76)
     • Acoustic preference

3. Focus Flow — LoRoom
   Score: 5.80 / 8.00
   Reasons:
     • Genre match (lofi)
     • Energy fit (1.80)
     • Acoustic preference

4. Spacewalk Thoughts — Orbit Bloom
   Score: 4.96 / 8.00
   Reasons:
     • Mood match (chill)
     • Energy fit (1.96)
     • Acoustic preference

5. Moonlight Sonata Reimagined — Classical Echo
   Score: 2.96 / 8.00
   Reasons:
     • Energy fit (1.96)
     • Acoustic preference

============================================================

============================================================
          TOP RECOMMENDATIONS — Deep Intense Rock           
============================================================

1. Storm Runner — Voltline
   Score: 6.88 / 8.00
   Reasons:
     • Genre match (rock)
     • Mood match (intense)
     • Energy fit (1.88)

2. Gym Hero — Max Pulse
   Score: 3.84 / 8.00
   Reasons:
     • Mood match (intense)
     • Energy fit (1.84)

3. Sunrise City — Neon Echo
   Score: 1.94 / 8.00
   Reasons:
     • Energy fit (1.94)

4. Crown Jewel — King Vibe
   Score: 1.94 / 8.00
   Reasons:
     • Energy fit (1.94)

5. Thunder Strikes — Iron Fist
   Score: 1.86 / 8.00
   Reasons:
     • Energy fit (1.86)

============================================================
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this

