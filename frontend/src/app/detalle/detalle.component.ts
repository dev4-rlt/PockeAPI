import { Component, Input } from '@angular/core';
import { PokemonDetail } from '../interfaces/pokemon-details';
import { DetallePokemonComponent } from '../detalle-pokemon/detalle-pokemon.component';
import { StatPokemonComponent } from "../stat-pokemon/stat-pokemon.component";

@Component({
  selector: 'app-detalle',
  standalone: true,
  imports: [DetallePokemonComponent, StatPokemonComponent],
  templateUrl: './detalle.component.html',
  styleUrl: './detalle.component.css'
})
export class DetalleComponent {

  @Input() details: PokemonDetail | null = null;
  
}
