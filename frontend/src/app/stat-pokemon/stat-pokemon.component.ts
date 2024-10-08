import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-stat-pokemon',
  standalone: true,
  imports: [],
  templateUrl: './stat-pokemon.component.html'
})
export class StatPokemonComponent {
  @Input({ required: true }) name!: string;
  @Input({ required: true }) value!: number;
}
