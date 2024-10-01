import { Component, Input, OnChanges, OnInit, SimpleChanges } from '@angular/core';
import { PokemonDetail } from '../interfaces/pokemon-details';
import { DetallePokemonComponent } from '../shared-components/detalle-pokemon/detalle-pokemon.component';
import { StatPokemonComponent } from "../stat-pokemon/stat-pokemon.component";
import { SeccionPokemonComponent } from '../shared-components/seccion-pokemon.component';
import { PokeapiService } from '../services/pokeapi.service';
import { HttpParams } from '@angular/common/http';

@Component({
  selector: 'app-pokemon-info',
  standalone: true,
  imports: [DetallePokemonComponent, StatPokemonComponent, SeccionPokemonComponent],
  templateUrl: './pokemon-info.component.html'
})
export class PokemonInfoComponent implements OnInit, OnChanges {

  @Input({ required: true }) codPokemon!: number;
  details: PokemonDetail | null = null;

  constructor(
    private pokemonService: PokeapiService
  ) {
  }

  ngOnChanges(changes: SimpleChanges): void {
    if (changes['codPokemon']) {
      this.getPokemonDetails();
    }
  }

  ngOnInit(): void {//Se ejecuta al renderizar el componente
  }

  getPokemonDetails(): void {
    let params = new HttpParams().append('codPokemon', this.codPokemon);

    this.pokemonService.getPokemonDetails(params).subscribe({
      next: async res => {
        this.details = res;

        let detailsSection = document.getElementById('details-section');
        detailsSection?.scrollIntoView({ behavior: 'smooth' });
      }, error: err => {
        console.log(err);
        alert('Ha ocurrido un error al obtener los detalles del Pokemon')
      }
    });
  }

}
