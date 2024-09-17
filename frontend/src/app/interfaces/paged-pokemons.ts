import { BasePokemon } from "./base-pokemon";

export type PagedPokemons = {
    count: number;
    next: string;
    previous: string;
    results: BasePokemon[];
}