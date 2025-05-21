import sqlite3

jokes_sample = [
    "Why don’t skeletons fight each other? They don’t have the guts.",
    "I’m reading a book on anti-gravity. It’s impossible to put down!",
    "Why did the scarecrow win an award? Because he was outstanding in his field.",
    "What do you call fake spaghetti? An impasta.",
    "Why don’t eggs tell jokes? They’d crack each other up.",
    "How does a penguin build its house? Igloos it together.",
    "Why did the math book look sad? Because it had too many problems.",
    "What do you call cheese that isn't yours? Nacho cheese.",
    "Why couldn’t the bicycle stand up by itself? It was two-tired.",
    "What do you call a factory that makes good products? A satisfactory.",
    "Why did the coffee file a police report? It got mugged.",
    "How do you organize a space party? You planet.",
    "Why did the tomato turn red? Because it saw the salad dressing!",
    "What do you call a fish wearing a bowtie? Sofishticated.",
    "Why do bees have sticky hair? Because they use honeycombs.",
    "How does a snowman get around? By riding an “icicle.”",
    "What do you call a belt made of watches? A waist of time.",
    "Why don’t scientists trust atoms? Because they make up everything.",
    "How do you catch a squirrel? Climb a tree and act like a nut.",
    "Why did the golfer bring two pairs of pants? In case he got a hole in one."
]

def create_db(db_name='dad_jokes_1000.db'):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jokes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            joke_text TEXT NOT NULL
        )
    ''')

    # Clear the table if it exists, to avoid duplicates on rerun
    cursor.execute('DELETE FROM jokes')

    for i in range(1000):
        base_joke = jokes_sample[i % len(jokes_sample)]
        joke_to_insert = base_joke if i < len(jokes_sample) else f"{base_joke} (Joke #{i+1})"
        cursor.execute("INSERT INTO jokes (joke_text) VALUES (?)", (joke_to_insert,))

    conn.commit()

    # Verify by counting rows
    cursor.execute('SELECT COUNT(*) FROM jokes')
    count = cursor.fetchone()[0]
    print(f"Inserted {count} jokes into '{db_name}'.")

    conn.close()

if __name__ == "__main__":
    create_db()