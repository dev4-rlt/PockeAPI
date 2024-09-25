import { Component, EventEmitter, Input, Output } from '@angular/core';
import { PokeapiService } from '../services/pokeapi.service';
import { RouterOutlet } from '@angular/router';
import { HttpParams } from '@angular/common/http';
import { BasePokemon } from '../interfaces/base-pokemon';

@Component({
  selector: 'app-listado',
  standalone: true,
  imports: [RouterOutlet],
  templateUrl: './listado.component.html'
})

export class ListadoComponent {

  @Output() codOutput = new EventEmitter<number>();

  basePokemons: BasePokemon[] | null = null;
  originalLocation: string;

  constructor(
    private pokemonService: PokeapiService
  ) {
    this.originalLocation = window.location.href;
    this.getPokemons();
  }

  getPokemons() {
    let params = new HttpParams().append('limit', 10).append('offset', 5);

    this.pokemonService.getBasePokemons(params).subscribe({
      next: res => {
        this.basePokemons = res;
      }, error: err => {
        this.basePokemons = null;
        console.log(err);
        alert("Ha ocurrido un error obteniendo los pokemons");
      }
    });

  }

  showPokemon(codPokemon: number) {
    this.codOutput.emit(codPokemon);
  }
}