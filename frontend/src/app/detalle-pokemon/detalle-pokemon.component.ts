import { NgClass } from '@angular/common';
import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-detalle-pokemon',
  standalone: true,
  imports: [NgClass],
  templateUrl: './detalle-pokemon.component.html',
  styleUrl: './detalle-pokemon.component.css'
})
export class DetallePokemonComponent {
  @Input({ required: true }) titulo!: string;
  @Input({ required: true }) descripcion!: string;
  @Input() backgroundColor: string = 'bg-white';
}
