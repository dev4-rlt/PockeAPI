import { Component, EventEmitter, Input, Output } from '@angular/core';
import { PokeapiService } from '../services/pokeapi.service';
import { RouterOutlet } from '@angular/router';
import { PagedPokemons } from '../interfaces/paged-pokemons';

@Component({
  selector: 'app-listado',
  standalone: true,
  imports: [RouterOutlet],
  templateUrl: './listado.component.html',
  styleUrl: './listado.component.css'
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
    this.pokemonService.getPagedPokemons().subscribe({
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
    setTimeout(() => {
      let detailsSection = document.getElementById('details-section');
      detailsSection?.scrollIntoView({behavior: 'smooth'});
    }, 100);
  }
}