import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-seccion-pokemon',
  standalone: true,
  imports: [],
  template: `
    <div class="mx-auto">
      <h3 class="text-center font-bold">{{title}}</h3>
      <div class="flex flex-row justify-center">
        <dl class="flex mt-3 sm:mt-5 space-x-2 sm:space-x-4 overflow-x-auto text-nowrap">
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
