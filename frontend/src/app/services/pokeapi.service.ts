import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class PokeapiService {

  API: string = 'https://pokeapi.co/api'

  constructor(private http: HttpClient) { }

  getPokemons() {
    return this.http.get(`${this.API}/v2/pokemon?limit=10&offset=20`);
  }
}
