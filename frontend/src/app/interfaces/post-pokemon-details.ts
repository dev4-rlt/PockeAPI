import { FormControl } from "@angular/forms";
import { Ability, Game, Move } from "./pokemon-details";


export interface AbilityForm {
    name: FormControl<string | null>;
    description: FormControl<string | null>;
}

export interface MoveForm {
    name: FormControl<string | null>;
    description: FormControl<string | null>;
}

export interface LocationForm {
    name: FormControl<string | null>;
}

export interface GameForm {
    name: FormControl<string | null>;
}

export type PostAbility = {
    name: string;
    description: string;
}

export type PostMove = {
    name: string;
    description: string;
}

export type PostLocation = {
    name: string;
}

export type PostGame = {
    name: string;
}

export type postCompletePokemon = {
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
    spriteFrontDefault: String;
    spriteFrontShiny: String;
    pokemonGames: Game[];
    pokemonHabilities: Ability[];
    pokemonLocations: Location[];
    pokemonMoves: Move[];
}