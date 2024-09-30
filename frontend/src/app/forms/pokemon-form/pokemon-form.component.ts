import { Component } from '@angular/core';
import { FormArray, FormControl, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { PokeapiService } from '../../services/pokeapi.service';
import { NgIf, NgClass } from '@angular/common';
import { AbilityFormComponent } from "../ability-form/ability-form.component";
import { AbilityForm, GameForm, LocationForm, MoveForm, PostAbility, postCompletePokemon, PostGame, PostLocation, PostMove } from '../../interfaces/post-pokemon-details';
import { MoveFormComponent } from '../move-form/move-form.component';
import { LocationFormComponent } from '../location-form/location-form.component';
import { GameFormComponent } from '../game-form/game-form.component';

@Component({
  selector: 'app-pokemon-form',
  standalone: true,
  imports: [ReactiveFormsModule, NgIf, NgClass, AbilityFormComponent, MoveFormComponent, LocationFormComponent, GameFormComponent],
  templateUrl: './pokemon-form.component.html'
})
export class PokemonFormComponent {

  pokemonForm = new FormGroup({
    name: new FormControl<string>('', [Validators.required, Validators.maxLength(30)]),
    height: new FormControl<number>(0, Validators.required),
    weight: new FormControl<number>(0, Validators.required),
    hp: new FormControl<number>(0, Validators.required),
    attack: new FormControl<number>(0, Validators.required),
    defense: new FormControl<number>(0, Validators.required),
    specialAttack: new FormControl<number>(0, Validators.required),
    specialDefense: new FormControl<number>(0, Validators.required),
    speed: new FormControl<number>(0, Validators.required),
    spriteFrontDefault: new FormControl<string>(''),
    spriteFrontShiny: new FormControl<string>(''),
    pokemonHabilities: new FormArray<FormGroup<AbilityForm>>([]),
    pokemonMoves: new FormArray<FormGroup<MoveForm>>([]),
    pokemonLocations: new FormArray<FormGroup<LocationForm>>([]),
    pokemonGames: new FormArray<FormGroup<GameForm>>([]),
  });

  showAbilityModal: boolean = false;
  showMoveModal: boolean = false;
  showLocationModal: boolean = false;
  showGameModal: boolean = false;

  constructor(
    private pokemonService: PokeapiService
  ) { }

  // Actualizar uno de los campos del formulario
  // this.pokemonForm.patchValue({
  //   name: 'nuevo name'
  // })

  createPokemon() {
    this.pokemonService.postCompletePokemon(this.pokemonForm.value as any).subscribe({
      next: res => {
        this.pokemonForm.reset();
        alert('El pokemon ' + res.name + ' ha sido guardado con éxito');
      }, error: err => {
        console.log(err);
        alert("Ha ocurrido un error inesperado durante la creación del pokemon, vuelva a intentarlo");
      }
    });
  }

  logForm(): void {
    console.log(this.pokemonForm);
  }

}
