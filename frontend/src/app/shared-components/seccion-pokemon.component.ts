import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-seccion-pokemon',
  standalone: true,
  imports: [],
  template: `
    <div class="mx-auto">
      <div class="text-base sm:text-xl md:text-2xl 2xl:text-3xl text-center font-bold text-gray-900">{{title}}</div>
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
