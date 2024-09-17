import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { PagedPokemons } from '../interfaces/paged-pokemons';
import { Observable } from 'rxjs';
import { AbilityDetails, PokemonDetail } from '../interfaces/pokemon-details';

@Injectable({
  providedIn: 'root'
})
export class PokeapiService {

  API: string = 'https://pokeapi.co/api'

  constructor(private http: HttpClient) { }

  getPagedPokemons(): Observable<PagedPokemons> {
    return this.http.get<PagedPokemons>(`${this.API}/v2/pokemon?limit=10&offset=20`);
  }

  getPokemonDetails(urlPokemon: string): Observable<PokemonDetail> {
    return this.http.get<PokemonDetail>(urlPokemon);
  }

  getAbilityDescription(urlAbility: string): Observable<AbilityDetails> {
    return this.http.get<AbilityDetails>(urlAbility);
  }

}
