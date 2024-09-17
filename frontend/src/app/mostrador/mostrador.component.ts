import { Component } from '@angular/core';
import { ListadoComponent } from '../listado/listado.component';
import { RouterOutlet } from '@angular/router';
import { DetalleComponent } from "../detalle/detalle.component";
import { DetallesService } from '../services/detalles.service';

@Component({
  selector: 'app-mostrador',
  standalone: true,
  imports: [RouterOutlet, ListadoComponent, DetalleComponent],
  templateUrl: './mostrador.component.html',
  styleUrl: './mostrador.component.css'
})
export class MostradorComponent {
  urlPokemon = '';
  ouputDetalle: string = '';

  details = {
    'name': '',
    'abilities': [{
      'name': '',
      'description': ''
    }],
  }

  //{ name: string; description: string; }[]; }

  constructor(private detailService: DetallesService
  ) {}

  getDetails() {
    this.detailService.getDetails(this.urlPokemon)
    .subscribe(
      async res => {
        let data: any = res;//corregir tipos
        this.details.name = data.name;
        this.details.abilities = [];
        for (let ability of data.abilities) {
          let description = await this.getAbilityDescription(ability.ability.url);
          this.details.abilities.push({
            'name': ability.ability.name,
            'description': typeof description === 'string'? description:''
          })
        }
      },
      err => {
        this.details = {
          'name': '',
          'abilities': [{
            'name': '',
            'description': ''
          }]
        }
        console.log(err);
        alert("Ha ocurrido un error obteniendo los detalles del pokemon");
      }
    )
  }

  async getAbilityDescription(url: string) {
    return new Promise((resolve, reject) => {
      this.detailService.getDetails(url)
      .subscribe(
        res => {
          let data: any = res;
          for (let effect of data.effect_entries) {
            if (effect.language.name == "en") {
              resolve(effect.effect);
            }
          }
        },
        err => {
          console.log(err);
          reject('')
        }
      )
    });
  }
}
