DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS top_measurements;
DROP TABLE IF EXISTS bottom_measurements;
DROP TABLE IF EXISTS general_features;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE top_measurements (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  shoulder_length DECIMAL,
  arm_length DECIMAL,
  chest_circum DECIMAL,
  abdomen_circum DECIMAL,
  FOREIGN KEY (user_id) REFERENCES user (id)
);

CREATE TABLE bottom_measurements (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  inseam_type TEXT,
  leg_length DECIMAL,
  waist_circum DECIMAL, 
  FOREIGN KEY (user_id) REFERENCES user (id)
);

CREATE TABLE general_features (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
-- THIS IS BEING DONE SINCE, SQLITE DOESN'T INHERENTLY
-- SUPPORT ENUMS
  ethnicity TEXT
    CHECK (ethnicity IN ('Indian', 'Asian', 'White', 'Black', 'Hispanic')),
  skin_tone INTEGER,
  body_type TEXT
      CHECK (body_type IN ('Lean', 'Stocky', 'Average', 'Athletic', 'XL')),
  height DECIMAL, -- In cms
  weighs DECIMAL,
  bmi_index DECIMAL,
  FOREIGN KEY (user_id) REFERENCES user (id)
);
