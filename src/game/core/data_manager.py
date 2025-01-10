import sqlite3
import os
import importlib.util
from collections import defaultdict
from datetime import datetime
from typing import TypedDict, List, Optional, Dict


class Timing(TypedDict):
    key_id: int
    time_point: float


class SongInfo(TypedDict):
    song_id: int
    name: str
    artist: str
    file_location: str
    timings: Optional[Dict[int, List[float]]]


class RunDetails(TypedDict):
    run_id: int
    song: SongInfo
    date: str
    score: int
    hits: int
    misses: int


class DataManager:
    def __init__(self, db_name='drum_machine_game.db', migrations_folder='migrations'):
        self.migrations_folder = migrations_folder
        self.db_name = db_name
        self.apply_migrations()

    def apply_migrations(self):
        # Connect to SQLite database
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        # Check if the migration table exists and create it if it does not
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS migration (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                migration_name TEXT NOT NULL UNIQUE,
                executed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()

        # Fetch list of already executed migrations
        cursor.execute('SELECT migration_name FROM migration')
        executed_migrations = set(row[0] for row in cursor.fetchall())

        # Get list of all migration files from the migrations folder
        migration_files = sorted(
            f for f in os.listdir(self.migrations_folder) if f.endswith('.sql') or f.endswith('.py'))

        for migration in migration_files:
            if migration in executed_migrations:
                continue  # Skip already executed migrations

            migration_path = os.path.join(self.migrations_folder, migration)
            if migration.endswith('.sql'):
                # Execute SQL file
                with open(migration_path, 'r') as file:
                    sql = file.read()
                    cursor.executescript(sql)
            elif migration.endswith('.py'):
                # Execute Python file
                spec = importlib.util.spec_from_file_location("migration_module", migration_path)
                migration_module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(migration_module)
                if hasattr(migration_module, 'run_migration'):
                    migration_module.run_migration(conn)  # Pass the connection to the Python migration

            # Mark the migration as executed
            cursor.execute('INSERT INTO migration (migration_name) VALUES (?)', (migration,))
            conn.commit()
            print(f"Migration '{migration}' applied.")

        conn.close()

    import sqlite3
    from collections import defaultdict

    def get_all_songs(self):
        """Retrieve all songs from the song table and include timings as a dictionary."""
        try:
            # Connect to the database
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            # Execute query to fetch all songs
            cursor.execute('SELECT id, name, artist, file_location FROM song')
            songs = cursor.fetchall()

            conn.close()

            # Return the list of songs with timings
            return [
                {
                    'id': song[0],
                    'name': song[1],
                    'artist': song[2],
                    'file_location': song[3],
                }
                for song in songs
            ]

        except sqlite3.Error as e:
            print(f"An error occurred while fetching songs: {e}")
            return []

    def get_song_details(self, song_id: int) -> Optional[SongInfo]:
        """
        Load a song with its timings grouped by key_id.

        Parameters:
            song_id (int): The ID of the song to retrieve.

        Returns:
            Optional[SongWithTimingsGrouped]: A dictionary containing the song details and a dictionary of timings
                                              grouped by key_id, or None if the song does not exist.
        """
        try:
            # Connect to the database
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            # Fetch song details
            cursor.execute('''
                SELECT id, name, artist, file_location
                FROM song
                WHERE id = ?
            ''', (song_id,))
            song_data = cursor.fetchone()

            if not song_data:
                print(f"No song found with ID {song_id}.")
                conn.close()
                return None

            # Fetch timings for the song and group by key_id
            cursor.execute('''
                SELECT key_id, time_point
                FROM timing
                WHERE song_id = ?
                ORDER BY key_id, time_point
            ''', (song_id,))
            timings_data = cursor.fetchall()

            conn.close()

            # Group timings by key_id
            timings_grouped = {}
            for key_id, time_point in timings_data:
                if key_id not in timings_grouped:
                    timings_grouped[key_id] = []
                timings_grouped[key_id].append(time_point)

            # Structure the output data
            return SongInfo(
                song_id=song_data[0],
                name=song_data[1],
                artist=song_data[2],
                file_location=song_data[3],
                timings=timings_grouped
            )

        except sqlite3.Error as e:
            print(f"An error occurred while fetching song with timings: {e}")
            return None

    def save_run_stats(self, song_id, button_presses):
        """
        Save stats for a run, including button presses, and return the run ID.

        Parameters:
            song_id (int): The ID of the song for this run.
            button_presses (list of dict): A list of dictionaries with each button press data.
                Each dictionary should have the following keys:
                - key_id (int): ID of the key pressed.
                - timing (float): Time at which the button was pressed.
                - accuracy_level (str): The accuracy level of the button press (e.g., 'Hit', 'Miss').

        Returns:
            int: The run ID if the run was saved successfully, None otherwise.
        """
        try:
            # Connect to the database
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            # Insert the run record
            date = datetime.now().isoformat()
            cursor.execute('INSERT INTO run (song_id, date) VALUES (?, ?)', (song_id, date))
            run_id = cursor.lastrowid  # Get the ID of the newly inserted run

            # Insert button presses for the run
            button_press_data = [
                (run_id, press['key_id'], press['timing'], press['accuracy_level'])
                for press in button_presses
            ]
            cursor.executemany('INSERT INTO button_press (run_id, key_id, timing, accuracy_level) VALUES (?, ?, ?, ?)',
                               button_press_data)

            # Commit and close the connection
            conn.commit()
            conn.close()

            print(f"Run stats for song ID {song_id} saved successfully with run ID {run_id}.")
            return run_id

        except sqlite3.Error as e:
            print(f"An error occurred while saving run stats: {e}")
            return None

    def get_best_run_score(self, song_id):
        """
        Retrieve the run with the highest score for a given song.
        Score calculation:
        - +10 points for each 'Hit'
        - -5 points for each 'Miss'

        Parameters:
            song_id (int): The ID of the song to find the best run for.

        Returns:
            dict: A dictionary containing the best run's details (run ID, date, score), or None if no runs exist.
        """
        try:
            # Connect to the database
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            # Query to calculate scores for each run
            # Todo: Extract scoring to some reusable code piece (something like a stored procedure, ...?)
            cursor.execute('''
                SELECT r.id, r.date,
                       SUM(CASE WHEN bp.accuracy_level = 'Hit' THEN 10
                                WHEN bp.accuracy_level = 'Miss' THEN -5
                                ELSE 0 END) AS score
                FROM run r
                JOIN button_press bp ON r.id = bp.run_id
                WHERE r.song_id = ?
                GROUP BY r.id
                ORDER BY score DESC, r.date ASC
                LIMIT 1
            ''', (song_id,))

            best_run = cursor.fetchone()
            conn.close()

            # Return the best run data as a dictionary
            if best_run:
                return {
                    'run_id': best_run[0],
                    'date': best_run[1],
                    'score': best_run[2]
                }
            else:
                print("No runs found for the given song ID.")
                return None

        except sqlite3.Error as e:
            print(f"An error occurred while retrieving the best run: {e}")
            return None

    def get_highscore(self, song_id) -> int:
        best_run = self.get_best_run_score(song_id)
        return best_run['score'] if best_run else 0

    def get_run_details(self, run_id: int) -> Optional[RunDetails]:
        """
        Fetch all relevant data for a given run, including song details, score, and the count of hits and misses.

        Parameters:
            run_id (int): The ID of the run to retrieve details for.

        Returns:
            Optional[RunDetails]: A dictionary containing the run details, song information, score, and hit/miss counts,
                                  or None if the run does not exist.
        """
        try:
            # Connect to the database
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            # Fetch the run details, including the song ID and date
            cursor.execute('''
                SELECT r.id, r.song_id, r.date, s.name, s.artist, s.file_location
                FROM run r
                JOIN song s ON r.song_id = s.id
                WHERE r.id = ?
            ''', (run_id,))
            run_data = cursor.fetchone()

            if not run_data:
                print(f"No run found with ID {run_id}.")
                conn.close()
                return None

            # Fetch counts of 'Hit' and 'Miss' accuracy levels and calculate score
            cursor.execute('''
                SELECT
                    SUM(CASE WHEN accuracy_level = 'Hit' THEN 1 ELSE 0 END) AS hits,
                    SUM(CASE WHEN accuracy_level = 'Miss' THEN 1 ELSE 0 END) AS misses
                FROM button_press
                WHERE run_id = ?
            ''', (run_id,))
            hit_miss_data = cursor.fetchone()
            hits = hit_miss_data[0] or 0
            misses = hit_miss_data[1] or 0

            # Calculate score
            score = (hits * 10) - (misses * 5)

            conn.close()

            # Structure the output data
            return RunDetails(
                run_id=run_data[0],
                song=SongInfo(
                    song_id=run_data[1],
                    name=run_data[3],
                    artist=run_data[4],
                    file_location=run_data[5]
                ),
                date=run_data[2],
                score=score,
                hits=hits,
                misses=misses
            )

        except sqlite3.Error as e:
            print(f"An error occurred while fetching run details: {e}")
            return None
