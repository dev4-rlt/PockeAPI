import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-seccion-pokemon',
  standalone: true,
  imports: [],
  template: `
    <div class="mx-auto max-w-2xl lg:max-w-7xl">
      <p class="mt-6 text-lg font-bold leading-8 text-gray-900 sm:text-2xl">{{title}}</p>
      <ng-content></ng-content>
    </div>
  `,
  styles: ``
})
export class SeccionPokemonComponent {
  @Input({ required: true }) title!: string;
}
