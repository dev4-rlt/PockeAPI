import { Component } from '@angular/core';
import { ListadoComponent } from '../listado/listado.component';
import { RouterOutlet } from '@angular/router';
import { DetalleComponent } from "../detalle/detalle.component";

@Component({
  selector: 'app-mostrador',
  standalone: true,
  imports: [RouterOutlet, ListadoComponent, DetalleComponent],
  templateUrl: './mostrador.component.html'
})

export class MostradorComponent {
  url = '';
}
