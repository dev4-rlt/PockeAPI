export type Game = {
    gameCod: number;
    gameName: string;
}

export type Ability = {
    abilityCod: number;
    abilityName: string;
    abilityDescription: string;
}

export type Location = {
    locationCod: number;
    locationName: string;
}

export type Move = {
    moveCod: number;
    moveName: string;
    moveDescription: string;
}

export type PokemonDetail = {
    codPokemon: number;
    name: string;
    attack: number;
    defense: number;
    height: number;
    weight: number;
    hp: number;
    specialAttack: number;
    specialDefense: number;
    speed: number;
    pokemonGames: Game[];
    pokemonHabilities: Ability[];
    pokemonLocations: Location[];
    pokemonMoves: Move[];
    spriteFrontDefault: String;
    spriteFrontShiny: String;
}