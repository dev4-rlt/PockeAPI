import { Component, Input } from '@angular/core';
import { PokemonDetail } from '../interfaces/pokemon-details';

@Component({
  selector: 'app-detalle',
  standalone: true,
  imports: [],
  templateUrl: './detalle.component.html',
  styleUrl: './detalle.component.css'
})
export class DetalleComponent {

  @Input() details: PokemonDetail | null = null;

  
}
