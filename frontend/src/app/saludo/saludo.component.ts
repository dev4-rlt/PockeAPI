import { Component } from '@angular/core';
import { RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-saludo',
  standalone: true,
  imports: [RouterOutlet, RouterLink, RouterLinkActive],
  templateUrl: './saludo.component.html'
})
export class SaludoComponent {

  constructor() {
    document.title = 'Bienvenido'
  }
}
