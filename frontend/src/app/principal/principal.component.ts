import { Component, OnInit } from '@angular/core';
import { PokemonListComponent } from '../pokemon-list/pokemonList.component';
import { Router, RouterOutlet } from '@angular/router';
import { PokemonInfoComponent } from "../pokemon-info/pokemon-info.component";
import { StorageService } from '../services/storage.service';

@Component({
  selector: 'app-principal',
  standalone: true,
  imports: [RouterOutlet, PokemonListComponent, PokemonInfoComponent],
  templateUrl: './principal.component.html'
})

export class PrincipalComponent implements OnInit {
  codPokemon: number | null = null;

  constructor(
    private storageService: StorageService,
    private router: Router
  ) {
  }

  ngOnInit(): void {
    if (this.storageService.name == '') {
      this.router.navigate(['login']);
    }
    document.title = 'Lista de Pokemons';
  }

}
