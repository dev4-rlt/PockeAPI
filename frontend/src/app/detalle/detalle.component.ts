import { Component, Input, OnChanges, OnInit, SimpleChanges } from '@angular/core';
import { Location, LocationInfo, LocationName, PokemonDetail } from '../interfaces/pokemon-details';
import { DetallePokemonComponent } from '../shared-components/detalle-pokemon/detalle-pokemon.component';
import { StatPokemonComponent } from "../stat-pokemon/stat-pokemon.component";
import { SeccionPokemonComponent } from '../shared-components/seccion-pokemon.component';
import { PokeapiService } from '../services/pokeapi.service';

@Component({
  selector: 'app-detalle',
  standalone: true,
  imports: [DetallePokemonComponent, StatPokemonComponent, SeccionPokemonComponent],
  templateUrl: './detalle.component.html'
})
export class DetalleComponent implements OnInit, OnChanges {

  @Input({ required: true }) urlPokemon!: string;
  details: PokemonDetail | null = null;

  constructor(
    private pokemonService: PokeapiService
  ) {
  }

  ngOnChanges(changes: SimpleChanges): void {
    if (changes['urlPokemon']) {
      this.getPokemonDetails();
    }
  }

  ngOnInit(): void {//Se ejecuta al renderizar el componente
  }

  getPokemonDetails(): void {
    this.pokemonService.getPokemonDetails(this.urlPokemon).subscribe({
      next: async res => {
        this.details = res;
        for (let abilityInfo of this.details.abilities) {
          let description = await this.getEffectDescription(abilityInfo.ability.url);
          abilityInfo.ability.description = (typeof (description) === 'string') ? description : ''
        }
        let detailsSection = document.getElementById('details-section');
        detailsSection?.scrollIntoView({ behavior: 'smooth' });

        for (let moveInfo of this.details.moves) {
          let description = await this.getEffectDescription(moveInfo.move.url);
          moveInfo.move.description = (typeof (description) === 'string' && description.length > 0) ? description : 'Sin descripción';
        }

        const locations = await this.getLocations(this.details.location_area_encounters);
        let locationNames = [];
        for (let location of locations) {
          let locationName = await this.getLocationName(location.location_area.url)
          let words: string[] = locationName.location.name.split('-')
          locationName.location.name = '';
          for (let word of words) {
            locationName.location.name += word.charAt(0).toUpperCase() + word.slice(1, word.length) + ' ';
          }
          locationNames.push(locationName);
        }
        this.details.locations = locationNames
      }, error: err => {
        console.log(err);
        alert('Ha ocurrido un error al obtener los detalles del Pokemon')
      }
    });
  }

  async getEffectDescription(url: string): Promise<string> {
    return new Promise((resolve, reject) => {
      this.pokemonService.getEffectDescription(url).subscribe({
        next: res => {
          for (let flavor_text_entrie of res.flavor_text_entries) {
            if (flavor_text_entrie.language.name == "en") {
              resolve(flavor_text_entrie.flavor_text);
            }
          }
          resolve('Sin descripción');
        }, error: err => {
          console.log(err);
          alert('Ha ocurrido un error al obtener la información del Pokemon')
          reject('')
        }
      });
    });
  }

  async getLocations(url: string): Promise<Location[]> {
    return new Promise((resolve, reject) => {
      this.pokemonService.getLocations(url).subscribe({
        next: res => {
          resolve(res);
        }, error: err => {
          console.log(err);
          alert('Ha ocurrido un error al obtener la información del Pokemon')
          reject(null)
        }
      });
    });
  }

  async getLocationName(url: string): Promise<LocationInfo> {
    return new Promise((resolve, reject) => {
      this.pokemonService.getLocationName(url).subscribe({
        next: res => {
          resolve(res);
        }, error: err => {
          console.log(err);
          alert('Ha ocurrido un error al obtener la información del Pokemon')
          reject(null)
        }
      });
    });
  }

}
