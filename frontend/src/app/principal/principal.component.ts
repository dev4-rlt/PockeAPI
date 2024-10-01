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

  ngOnInit(): void {
    document.title = 'Lista de Pokemons';
  }

}
