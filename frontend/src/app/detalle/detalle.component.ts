import { Component, Input } from '@angular/core';
import { PokemonDetail } from '../interfaces/pokemon-details';
import { DetallePokemonComponent } from '../shared-components/detalle-pokemon/detalle-pokemon.component';
import { StatPokemonComponent } from "../stat-pokemon/stat-pokemon.component";
import { SeccionPokemonComponent } from '../shared-components/seccion-pokemon.component';

@Component({
  selector: 'app-detalle',
  standalone: true,
  imports: [DetallePokemonComponent, StatPokemonComponent, SeccionPokemonComponent],
  templateUrl: './detalle.component.html'
})
export class DetalleComponent {

  @Input() details: PokemonDetail | null = null;
  
}
