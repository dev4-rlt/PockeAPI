import { NgClass } from '@angular/common';
import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-detalle-pokemon',
  standalone: true,
  imports: [NgClass],
  templateUrl: './detalle-pokemon.component.html',
})
export class DetallePokemonComponent {
  @Input({ required: true }) titulo!: string;
  @Input() descripcion: string | null = null;
  @Input({ required: true }) iconName!: string;
  @Input({ required: true }) iconColor: string = '';
  @Input() backgroundColor: string = 'bg-white';
}
