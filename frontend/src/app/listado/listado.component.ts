import { Component, EventEmitter, Input, Output } from '@angular/core';
import { PokeapiService } from '../services/pokeapi.service';
import { RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-listado',
  standalone: true,
  imports: [RouterOutlet],
  templateUrl: './listado.component.html',
  styleUrl: './listado.component.css'
})

export class ListadoComponent {
  
  @Output() urlOutput = new EventEmitter<string>();

  pokemonList: any = [];//Corregir tipo de dato

  constructor(
    private pokemonService: PokeapiService
  ) {
    this.getPokemons()
  }

  getPokemons() {
    this.pokemonService.getPokemons()
    .subscribe(
      res => {
        let data: any = res;//corregir tipos
        this.pokemonList = data.results;
      },
      err => {
        this.pokemonList = [];
        console.log(err);
        alert("Ha ocurrido un error obteniendo los pokemons");
      }
    )
  }

  showPokemon(urlPokemon: string) {
    this.urlOutput.emit(urlPokemon);
  }
}

type Pokemon = {
  name: string;
  url: string;
};