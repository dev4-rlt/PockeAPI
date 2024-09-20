import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-seccion-pokemon',
  standalone: true,
  imports: [],
  template: `
    <div class="mx-auto max-w-7xl">
      <p class="font-bold text-gray-900 sm:text-2xl">{{title}}</p>
      <div class="flex flex-row justify-center">
        <dl class="flex mt-5 space-x-4 p-2 overflow-x-auto text-nowrap">
          <ng-content class="items-center"></ng-content>
        </dl>
      </div>
    </div>
  `,
  styles: ``
})
export class SeccionPokemonComponent {
  @Input({ required: true }) title!: string;
}
