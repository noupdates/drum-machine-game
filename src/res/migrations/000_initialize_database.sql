-- 000_initialize_database.sql

-- Create the song table
CREATE TABLE IF NOT EXISTS song (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    artist TEXT NOT NULL,
    file_location TEXT NOT NULL
);

-- Create the timing table for key timings related to each song
CREATE TABLE IF NOT EXISTS timing (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    song_id INTEGER NOT NULL,
    key_id INTEGER NOT NULL,
    time_point FLOAT NOT NULL,
    FOREIGN KEY (song_id) REFERENCES song(id)
);

-- Create the run table to store information about each game run
CREATE TABLE IF NOT EXISTS run (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    song_id INTEGER NOT NULL,
    date TEXT NOT NULL,
    FOREIGN KEY (song_id) REFERENCES song(id)
);

-- Create the button_press table to store information about button presses during a run
CREATE TABLE IF NOT EXISTS button_press (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id INTEGER NOT NULL,
    key_id INTEGER NOT NULL,
    timing FLOAT NOT NULL,
    accuracy_level TEXT NOT NULL,
    FOREIGN KEY (run_id) REFERENCES run(id)
);

