CREATE TABLE pokemons (
    cod_pokemon         SERIAL PRIMARY KEY,
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

CREATE TABLE habilities (
    cod_hability    SERIAL PRIMARY KEY,
    name            VARCHAR(25) NOT NULL,
    description     VARCHAR(255)
);

CREATE TABLE pokemon_habilities (
    cod_pokemon_hability    SERIAL PRIMARY KEY,
    pokemon_cod             INT NOT NULL,
    hability_cod            INT NOT NULL,
    CONSTRAINT fk_pokemon FOREIGN KEY(pokemon_cod) REFERENCES pokemons(cod_pokemon),
    CONSTRAINT fk_hability FOREIGN KEY(hability_cod) REFERENCES habilities(cod_hability)
);

CREATE TABLE moves (
    cod_move        SERIAL PRIMARY KEY,
    name            VARCHAR(25) NOT NULL,
    description     VARCHAR(255)
);

CREATE TABLE pokemon_moves (
    cod_pokemon_move   SERIAL PRIMARY KEY,
    pokemon_cod        INT NOT NULL,
    move_cod           INT NOT NULL,
    FOREIGN KEY(pokemon_cod) REFERENCES pokemons(cod_pokemon),
    FOREIGN KEY(move_cod) REFERENCES moves(cod_move)
);

CREATE TABLE locations (
    cod_locations       SERIAL PRIMARY KEY,
    name                VARCHAR(25) NOT NULL
);

CREATE TABLE pokemon_locations (
    cod_pokemon_location        SERIAL PRIMARY KEY,
    pokemon_cod                 INT NOT NULL,
    location_cod                INT NOT NULL,
    FOREIGN KEY(pokemon_cod) REFERENCES pokemons(cod_pokemon),
    FOREIGN KEY(location_cod) REFERENCES locations(cod_location)
);

CREATE TABLE games (
    cod_game     SERIAL PRIMARY KEY,
    name        VARCHAR(25) NOT NULL
);

CREATE TABLE pokemon_games (
    cod_pokemon_game        SERIAL PRIMARY KEY,
    pokemon_cod             INT NOT NULL,
    game_cod                INT NOT NULL,
    FOREIGN KEY(pokemon_cod) REFERENCES pokemons(cod_pokemon),
    FOREIGN KEY(game_cod) REFERENCES games(cod_game)
);