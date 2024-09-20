CREATE TABLE pokemon (
    id                  INT PRIMARY KEY,
    name                VARCHAR(25) NOT NULL,
    height              INT NOT NULL,
    weight              INT NOT NULL,
    hp                  INT NOT NULL,
    attack              INT NOT NULL,
    defense             INT NOT NULL,
    special_attack      INT NOT NULL,
    special_defense     INT NOT NULL,
    speed               INT NOT NULL
);

CREATE TABLE hability (
    id              INT SERIAL PRIMARY KEY,
    name            VARCHAR(25) NOT NULL,
    description     VARCHAR(255)
);

CREATE TABLE pokemon_hability (
    id_pokemon      INT,
    id_hability     INT,
    FOREIGN_KEY(id_pokemon) REFERENCES pokemons(id_pokemon),
    FOREIGN_KEY(id_hability) REFERENCES habilities(id_hability),
    PRIMARY_KEY(id_pokemon, id_hability),
);

CREATE TABLE move (
    id              INT SERIAL PRIMARY KEY,
    name            VARCHAR(25) NOT NULL,
    description     VARCHAR(255)
);

CREATE TABLE pokemon_move (
    id_pokemon      INT,
    id_move         INT,
    FOREIGN_KEY(id_pokemon) REFERENCES pokemons(id_pokemon),
    FOREIGN_KEY(id_move) REFERENCES moves(id_move),
    PRIMARY_KEY(id_pokemon, id_move),
)

CREATE TABLE location (
    id      INT SERIAL PRIMARY KEY,
    name    VARCHAR(25) NOT NULL
);

CREATE TABLE pokemon_location (
    id_pokemon      INT,
    id_location     INT,
    FOREIGN_KEY(id_pokemon) REFERENCES pokemons(id_pokemon),
    FOREIGN_KEY(id_location) REFERENCES moves(id_location),
    PRIMARY_KEY(id_pokemon, id_location),
)

CREATE TABLE game (
    id      INT SERIAL PRIMARY KEY,
    name    VARCHAR(25) NOT NULL
);

CREATE TABLE pokemon_game (
    id_pokemon      INT,
    id_game         INT,
    FOREIGN_KEY(id_pokemon) REFERENCES pokemons(id_pokemon),
    FOREIGN_KEY(id_game) REFERENCES moves(id_game),
    PRIMARY_KEY(id_pokemon, id_game),
)