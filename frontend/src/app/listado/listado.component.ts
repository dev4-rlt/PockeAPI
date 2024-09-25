import { Component, EventEmitter, Output } from '@angular/core';
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
  offsetPokemons: number = 0;
  limitPokemons: number = 25;

  constructor(
    private pokemonService: PokeapiService
  ) {
    this.getPokemons();
  }

  blockAdvanceButton() {
    let advanceButton = document.getElementById('advanceButton');
    if (advanceButton) advanceButton.className = 'fa-solid fa-3x fa-chevron-right text-gray-500 ml-10 my-auto cursor-not-allowed';
  }

  allowAdvanceButton() {
    let advanceButton = document.getElementById('advanceButton');
    if (advanceButton) advanceButton.className = 'fa-solid fa-3x fa-chevron-right text-blue-950 ml-10 my-auto cursor-pointer';
  }

  blockBackButton() {
    let backButton = document.getElementById('backButton');
    if (backButton) backButton.className = 'fa-solid fa-3x fa-chevron-left text-gray-500 mr-10 my-auto cursor-not-allowed';
  }

  allowBackButton() {
    let backButton = document.getElementById('backButton');
    if (backButton) backButton.className = 'fa-solid fa-3x fa-chevron-left text-blue-950 mr-10 my-auto cursor-pointer';
  }

  getPokemons() {
    let params = new HttpParams().append('offset', this.offsetPokemons).append('limit', this.limitPokemons);

    this.pokemonService.getBasePokemons(params).subscribe({
      next: res => {
        if (res.length > 0) {
          this.basePokemons = res;
          if (res.length < this.limitPokemons) {
            this.blockAdvanceButton();
          }
        } else {
          this.offsetPokemons -= this.limitPokemons;
          this.blockAdvanceButton();
        }
      }, error: err => {
        this.basePokemons = null;
        console.log(err);
        alert("Ha ocurrido un error obteniendo los pokemons");
      }
    });
  }

  advance(){
    this.offsetPokemons += this.limitPokemons;
    if (this.offsetPokemons > 0) {
      this.allowBackButton();
    }
    this.getPokemons();
  }
  
  back(){
    this.offsetPokemons -= this.limitPokemons;
    if (this.offsetPokemons <= 0) {
      this.offsetPokemons = 0;
      this.blockBackButton;
    } else if (this.offsetPokemons > this.limitPokemons) {
      this.allowAdvanceButton();
    }
    this.getPokemons();
  }
  
  showPokemon(codPokemon: number) {
    this.codOutput.emit(codPokemon);
  }
}