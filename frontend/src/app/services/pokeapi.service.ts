import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { PagedPokemon } from '../interfaces/paged-pokemon';
import { Observable } from 'rxjs';
import { PokemonDetail } from '../interfaces/pokemon-details';

@Injectable({
  providedIn: 'root'
})
export class PokeapiService {

  API: string = 'http://127.0.0.1:5000'

  constructor(private http: HttpClient) { }

  getPagedPokemons(params: HttpParams): Observable<PagedPokemon> {
    return this.http.get<PagedPokemon>(`${this.API}/pokemons`, { params: params});
  }

  getPokemonDetails(params: HttpParams): Observable<PokemonDetail> {
    return this.http.get<PokemonDetail>(`${this.API}/pokemons/details`, { params: params});
  }

}
