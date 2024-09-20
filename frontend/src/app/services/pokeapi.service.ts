import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { PagedPokemons } from '../interfaces/paged-pokemons';
import { Observable } from 'rxjs';
import { EffectDetails, Location, LocationInfo, PokemonDetail } from '../interfaces/pokemon-details';

@Injectable({
  providedIn: 'root'
})
export class PokeapiService {

  API: string = 'http://127.0.0.1:5000'

  constructor(private http: HttpClient) { }

  getPagedPokemons(params: HttpParams): Observable<PagedPokemons> {
    return this.http.get<PagedPokemons>(`${this.API}/pokemons`, { params: params});
  }

  getPokemonDetails(urlPokemon: string): Observable<PokemonDetail> {
    return this.http.get<PokemonDetail>(urlPokemon);
  }

  getEffectDescription(urlEffect: string): Observable<EffectDetails> {
    return this.http.get<EffectDetails>(urlEffect);
  }

  getLocations(urlLocations: string): Observable<Location[]> {
    return this.http.get<Location[]>(urlLocations);
  }

  getLocationName(urlLocation: string): Observable<LocationInfo> {
    return this.http.get<LocationInfo>(urlLocation);
  }

}
