import { Component, OnInit } from '@angular/core';
import { ListadoComponent } from '../listado/listado.component';
import { RouterOutlet } from '@angular/router';
import { DetalleComponent } from "../detalle/detalle.component";

@Component({
  selector: 'app-mostrador',
  standalone: true,
  imports: [RouterOutlet, ListadoComponent, DetalleComponent],
  templateUrl: './mostrador.component.html'
})

export class MostradorComponent implements OnInit {
  codPokemon: number | null = null;

  constructor() {
  }

  ngOnInit(): void {
    document.title = 'Lista de Pokemons';
  }

}
