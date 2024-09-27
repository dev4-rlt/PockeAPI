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
  pageNumber: number = 1;
  perPage: number = 25;
  totalPages: number = 0;
  selectedPokemon: number | null = null;

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
    let params = new HttpParams().append('page', this.pageNumber).append('per_page', this.perPage);
    this.pokemonService.getPagedPokemons(params).subscribe({
      next: res => {
        if (res.page == res.pages) {
          this.blockAdvanceButton();
        }
        this.totalPages = res.pages;
        this.basePokemons = res.items;
      }, error: err => {
        this.basePokemons = null;
        console.log(err);
        alert("Ha ocurrido un error obteniendo los pokemons");
      }
    });
  }

  advance() {
    this.pageNumber++;
    if (this.pageNumber > this.totalPages) {
      this.pageNumber--;
    } else {
      if (this.pageNumber > 1) {
        this.allowBackButton();
      }
      this.getPokemons();
    }
  }
  
  back(){
    this.pageNumber--;
    if (this.pageNumber <= 1) {
      this.pageNumber = 1;
      this.blockBackButton();
    } else if (this.pageNumber < this.totalPages) {
      this.allowAdvanceButton();
    }
    this.getPokemons();
  }
  
  showPokemon(codPokemon: number) {
    this.selectedPokemon = codPokemon;
    this.codOutput.emit(codPokemon);
  }
}