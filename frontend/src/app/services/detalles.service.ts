import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class DetallesService {

  constructor(private http: HttpClient) { }

  getDetails(urlPokemon: string) {
    return this.http.get(urlPokemon);
  }

}
