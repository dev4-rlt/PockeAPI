import { Component, EventEmitter, Input, Output } from '@angular/core';
import { PokeapiService } from '../services/pokeapi.service';
import { RouterOutlet } from '@angular/router';
import { PagedPokemons } from '../interfaces/paged-pokemons';
import { HttpParams } from '@angular/common/http';

@Component({
  selector: 'app-listado',
  standalone: true,
  imports: [RouterOutlet],
  templateUrl: './listado.component.html'
})

export class ListadoComponent {

  @Output() urlOutput = new EventEmitter<string>();

  pagedPokemons: PagedPokemons | null = null;//Corregir tipo de dato
  originalLocation: string;

  constructor(
    private pokemonService: PokeapiService
  ) {
    this.originalLocation = window.location.href;
    this.getPokemons();
  }

  getPokemons() {
    let params = new HttpParams().append('limit', 5).append('offset', 5);

    this.pokemonService.getPagedPokemons(params).subscribe({
      next: res => {
        this.pagedPokemons = res;
      }, error: err => {
        this.pagedPokemons = null;
        console.log(err);
        alert("Ha ocurrido un error obteniendo los pokemons");
      }
    });

  }

  showPokemon(urlPokemon: string) {
    this.urlOutput.emit(urlPokemon);
  }
}