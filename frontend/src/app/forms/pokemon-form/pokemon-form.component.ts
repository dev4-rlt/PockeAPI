import { Component } from '@angular/core';
import { FormControl, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { PostPokemon } from '../../interfaces/base-pokemon';
import { PokeapiService } from '../../services/pokeapi.service';
import { NgIf, NgClass } from '@angular/common';
import { FieldPokemon } from '../../interfaces/field-pokemon';
import { AbilityFormComponent } from "../ability-form/ability-form.component";
import { PostAbility, PostGame, PostLocation, PostMove } from '../../interfaces/post-pokemon-details';
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

  fields: FieldPokemon[] = [
    { id: 'name', name: 'Nombre', required: true },
    { id: 'height', name: 'Altura', required: true },
    { id: 'hp', name: 'Puntos de vida', required: true },
    { id: 'attack', name: 'Ataque', required: true },
    { id: 'defense', name: 'Defensa', required: true },
    { id: 'specialAttack', name: 'Ataque especial', required: true },
    { id: 'specialDefense', name: 'Defensa especial', required: true },
    { id: 'speed', name: 'Velocidad', required: true },
    { id: 'spriteFrontDefault', name: 'Enlace de imagen default', required: false },
    { id: 'spriteFrontShiny', name: 'Enlace de imagen resplandeciente', required: false }
  ];

  pokemonForm: FormGroup = new FormGroup({
    name: new FormControl<string>('', [Validators.required, Validators.maxLength(10)]),
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
    pokemonHabilitities: new FormControl<PostAbility[]>([]),
    pokemonMoves: new FormControl<PostAbility[]>([]),
    pokemonLocations: new FormControl<PostAbility[]>([]),
    pokemonGames: new FormControl<PostAbility[]>([]),
  });

  abilityModalDisplay = 'hidden';
  moveModalDisplay = 'hidden';
  locationModalDisplay = 'hidden';
  gameModalDisplay = 'hidden';

  constructor(
    private pokemonService: PokeapiService
  ) { }

  // Actualizar uno de los campos del formulario
  // this.pokemonForm.patchValue({
  //   name: 'nuevo name'
  // })

  createPokemon() {
    this.pokemonService.postPokemon(this.pokemonForm.value).subscribe({
      next: res => {
        this.pokemonForm.reset();
        alert('El pokemon ' + res.name + ' ha sido guardado con éxito');
      }, error: err => {
        console.log(err);
        alert("Credenciales incorrectas");
      }
    });
  }

  hideAbilityForm() {
    this.abilityModalDisplay = 'hidden';
  }

  showAbilityForm() {
    this.abilityModalDisplay = 'flex';
  }

  hideMoveForm() {
    this.moveModalDisplay = 'hidden';
  }

  showMoveForm() {
    this.moveModalDisplay = 'flex';
  }

  hideLocationForm() {
    this.locationModalDisplay = 'hidden';
  }

  showLocationForm() {
    this.locationModalDisplay = 'flex';
  }

  hideGameForm() {
    this.gameModalDisplay = 'hidden';
  }

  showGameForm() {
    this.gameModalDisplay = 'flex';
  }

  saveAbility(ability: PostAbility) {
    this.pokemonForm.value.pokemonHabilitities.push(ability);
    this.hideAbilityForm();
  }

  saveMove(move: PostMove) {
    this.pokemonForm.value.pokemonMoves.push(move)
    this.hideMoveForm();
  }

  saveLocation(location: PostLocation) {
    this.pokemonForm.value.pokemonLocations.push(location)
    this.hideLocationForm();
  }

  saveGame(game: PostGame) {
    this.pokemonForm.value.pokemonGames.push(game)
    this.hideGameForm();
  }

  logForm(): void {
    console.log(this.pokemonForm);
    
  }

}
