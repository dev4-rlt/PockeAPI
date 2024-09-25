import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { BasePokemon } from '../interfaces/base-pokemon';
import { Observable } from 'rxjs';
import { Location, PokemonDetail } from '../interfaces/pokemon-details';

@Injectable({
  providedIn: 'root'
})
export class PokeapiService {

  API: string = 'http://127.0.0.1:5000'

  constructor(private http: HttpClient) { }

  getBasePokemons(params: HttpParams): Observable<BasePokemon[]> {
    return this.http.get<BasePokemon[]>(`${this.API}/pokemons`, { params: params});
  }

  getPokemonDetails(params: HttpParams): Observable<PokemonDetail> {
    return this.http.get<PokemonDetail>(`${this.API}/pokemons/details`, { params: params});
  }

}
