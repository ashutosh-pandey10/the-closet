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
  shoulder_length DECIMAL NOT NULL,
  arm_length DECIMAL NOT NULL,
  chest_circum DECIMAL NOT NULL,
  abdomen_circum DECIMAL NOT NULL,
  FOREIGN KEY (user_id) REFERENCES user (id)
);

CREATE TABLE bottom_measurements (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  inseam_type TEXT NOT NULL,
  leg_length DECIMAL NOT NULL,
  waist_circum DECIMAL NOT NULL, 
  FOREIGN KEY (user_id) REFERENCES user (id)
);

CREATE TABLE general_features (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
-- THIS IS BEING DONE SINCE, SQLITE DOESN'T INHERENTLY
-- SUPPORT ENUMS
  ethnicity TEXT NOT NULL
    CHECK (ethnicity IN ('Indian', 'Asian', 'White', 'Black', 'Hispanic')),
  skin_tone INTEGER NOT NULL,
  body_type TEXT NOT NULL
      CHECK (ethnicity IN ('Lean', 'Stocky', 'Average', 'Athletic', 'XL')),
  height DECIMAL NOT NULL, -- In cms
  weighs DECIMAL NOT NULL,
  bmi_index DECIMAL,
  FOREIGN KEY (user_id) REFERENCES user (id)
);