import { Component, EventEmitter, Output } from '@angular/core';
import { PokeapiService } from '../services/pokeapi.service';
import { RouterOutlet } from '@angular/router';
import { HttpParams } from '@angular/common/http';
import { BasePokemon } from '../interfaces/base-pokemon';
import { NgClass } from '@angular/common';

@Component({
  selector: 'app-listado',
  standalone: true,
  imports: [RouterOutlet, NgClass],
  templateUrl: './listado.component.html'
})

export class ListadoComponent {

  @Output() codOutput = new EventEmitter<number>();

  basePokemons: BasePokemon[] | null = null;
  offsetPokemons: number = 0;
  limitPokemons: number = 25;

  backButtonColor: string = 'text-gray-500';
  backButtonCursor: string = 'cursor-not-allowed';
  advanceButtonColor: string = 'text-blue-950';
  advanceButtonCursor: string = 'cursor-pointer';

  constructor(
    private pokemonService: PokeapiService
  ) {
    this.getPokemons();
  }

  blockAdvanceButton() {
    this.advanceButtonColor = 'text-gray-500';
    this.advanceButtonCursor = 'cursor-not-allowed';
  }

  allowAdvanceButton() {
    this.advanceButtonColor = 'text-blue-950';
    this.advanceButtonCursor = 'cursor-pointer';
  }

  blockBackButton() {
    this.backButtonColor = 'text-gray-500';
    this.backButtonCursor = 'cursor-not-allowed';
  }

  allowBackButton() {
    this.backButtonColor = 'text-blue-950';
    this.backButtonCursor = 'cursor-pointer';
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