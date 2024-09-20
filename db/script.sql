CREATE TABLE pokemons (
    id                  INT PRIMARY KEY,
    name                VARCHAR(25),
    height              INT,
    weight              INT,
    hp                  INT,
    attack              INT,
    defense             INT,
    special_attack      INT,
    special_defense     INT,
    speed               INT
);

CREATE TABLE hailities (
    id              INT SERIAL PRIMARY KEY,
    name            VARCHAR(25),
    description     VARCHAR(255)
);

CREATE TABLE hability_pokemon (
    id_pokemon      INT,
    id_hability     INT,
    FOREIGN_KEY(id_pokemon) REFERENCES pokemons(id_pokemon),
    FOREIGN_KEY(id_hability) REFERENCES habilities(id_hability),
    PRIMARY_KEY(id_pokemon, id_hability),
);

CREATE TABLE moves (
    id              INT SERIAL PRIMARY KEY,
    name            VARCHAR(25),
    description     VARCHAR(255)
);

CREATE TABLE pokemon_move (
    id_pokemon      INT,
    id_move         INT,
    FOREIGN_KEY(id_pokemon) REFERENCES pokemons(id_pokemon),
    FOREIGN_KEY(id_move) REFERENCES moves(id_move),
    PRIMARY_KEY(id_pokemon, id_move),
)

CREATE TABLE locations (
    id      INT SERIAL PRIMARY KEY,
    name    VARCHAR(25)
);

CREATE TABLE pokemon_location (
    id_pokemon      INT,
    id_location     INT,
    FOREIGN_KEY(id_pokemon) REFERENCES pokemons(id_pokemon),
    FOREIGN_KEY(id_location) REFERENCES moves(id_location),
    PRIMARY_KEY(id_pokemon, id_location),
)

CREATE TABLE games (
    id      INT SERIAL PRIMARY KEY,
    name    VARCHAR(25)
);

CREATE TABLE pokemon_game (
    id_pokemon      INT,
    id_game         INT,
    FOREIGN_KEY(id_pokemon) REFERENCES pokemons(id_pokemon),
    FOREIGN_KEY(id_game) REFERENCES moves(id_game),
    PRIMARY_KEY(id_pokemon, id_game),
)