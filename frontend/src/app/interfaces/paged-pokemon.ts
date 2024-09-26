import { BasePokemon } from "./base-pokemon"

export type PagedPokemon = {
    page: number,
    per_page: number,
    pages: number,
    total: number,
    items:  BasePokemon[]
}