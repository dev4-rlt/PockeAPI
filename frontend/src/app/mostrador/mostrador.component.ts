import { Component } from '@angular/core';
import { ListadoComponent } from '../listado/listado.component';
import { RouterOutlet } from '@angular/router';
import { DetalleComponent } from "../detalle/detalle.component";
import { PokeapiService } from '../services/pokeapi.service';
import { PokemonDetail } from '../interfaces/pokemon-details';

@Component({
  selector: 'app-mostrador',
  standalone: true,
  imports: [RouterOutlet, ListadoComponent, DetalleComponent],
  templateUrl: './mostrador.component.html',
  styleUrl: './mostrador.component.css'
})
export class MostradorComponent {
  urlPokemon = '';
  ouputDetalle: string = '';

  details: PokemonDetail | null = null;

  constructor(
    private pokemonService: PokeapiService
  ) {}

  getDetails() {
    this.pokemonService.getPokemonDetails(this.urlPokemon).subscribe({
      next: async res => {
        this.details = res;
        for (let abilityInfo of this.details.abilities) {
          let description =  await this.getEffectDescription(abilityInfo.ability.url);
          abilityInfo.ability.description = (typeof(description) === 'string')? description : ''
        }
        for (let moveInfo of this.details.moves) {
          let description =  await this.getEffectDescription(moveInfo.move.url);
          moveInfo.move.description = (typeof(description) === 'string' && description.length > 0)? description : 'Sin descripción'
        }
      }, error: err => {
        console.log(err);
        alert('Ha ocurrido un error al obtener los detalles del Pokemon')
      }
    });
  }

  async getEffectDescription(url: string) {
    return new Promise((resolve, reject) => {
      this.pokemonService.getEffectDescription(url).subscribe({
        next: res => {
          for (let flavor_text_entrie of res.flavor_text_entries) {
            if (flavor_text_entrie.language.name == "en") {
              resolve(flavor_text_entrie.flavor_text);
            }
          }
        }, error: err => {
          console.log(err);
          alert('Ha ocurrido un error al obtener la información del Pokemon')
          reject('')
        }
      });
    });
  }
}
