import { Component, EventEmitter, OnInit, Output } from '@angular/core';
import { PokeapiService } from '../services/pokeapi.service';
import { RouterOutlet } from '@angular/router';
import { HttpParams } from '@angular/common/http';
import { BasePokemon } from '../interfaces/base-pokemon';
import { NgClass } from '@angular/common';
import { FormGroup, FormControl, ReactiveFormsModule } from '@angular/forms';

@Component({
  selector: 'app-pokemon-list',
  standalone: true,
  imports: [RouterOutlet, NgClass, ReactiveFormsModule],
  templateUrl: './pokemonList.component.html'
})

export class PokemonListComponent implements OnInit {

  @Output() codOutput = new EventEmitter<number | null>();

  basePokemons: BasePokemon[] | null = null;
  
  pageNumber: number = 1;
  perPage: number = 25;
  totalPages: number = 0;
  totalPokemons: number = 0;
  selectedPokemon: number | null = null;

  advanceButtonDisabled = false;
  backButtonDisabled = true;

  searchForm: FormGroup = new FormGroup({
    keyword: new FormControl<string>('')
  });

  constructor(
    private pokemonService: PokeapiService
  ) {
  }

  ngOnInit(): void {
    this.getPokemons();
  }

  getPokemons() {
    let params = new HttpParams().append('page', this.pageNumber).append('per_page', this.perPage);
    if (this.searchForm.value.keyword != '') {//Se realiza una búsqueda
      params = params.append('name', this.searchForm.value.keyword);
    }
    this.pokemonService.getPagedPokemons(params).subscribe({
      next: res => {
        this.advanceButtonDisabled = res.page == res.pages;
        this.backButtonDisabled = res.page == 1;
        
        this.totalPages = res.pages;
        this.basePokemons = res.items;
        this.totalPokemons = res.total;
      }, error: err => {
        this.basePokemons = null;
        console.log(err);
        alert("Ha ocurrido un error obteniendo los pokemons");
      }
    });
  }

  filterPokemons(){
    this.pageNumber = 1;
    this.getPokemons();
  }

  // filterPokemons() {
  //   if (this.searchForm.invalid) {
  //     this.filteredPokemons = this.basePokemons;
  //     return;
  //   }
  //   let coincidences = this.basePokemons?.filter(
  //     basePokemon => basePokemon.name.toLowerCase().includes(this.searchForm.value.keyword.toLowerCase())
  //   );
  //   this.filteredPokemons = coincidences? coincidences:null;
  // }

  advance() {
    if (this.pageNumber < this.totalPages) {
      this.pageNumber++;
      if (this.pageNumber > 1) {
        this.backButtonDisabled = false;
      }
      this.getPokemons();
    }
  }
  
  back(){
    if (this.pageNumber > 1) {
      this.pageNumber--;
      if (this.pageNumber == 1) {
        this.backButtonDisabled = true;
      }
    }
    if(this.pageNumber < this.totalPages) {
      this.advanceButtonDisabled = false;
    }
    this.getPokemons();
  }
  
  showPokemon(codPokemon: number) {
    if (this.selectedPokemon == codPokemon) {
      this.selectedPokemon = null;
      this.codOutput.emit(null);
      return
    }
    this.selectedPokemon = codPokemon;
    this.codOutput.emit(codPokemon);
  }
}