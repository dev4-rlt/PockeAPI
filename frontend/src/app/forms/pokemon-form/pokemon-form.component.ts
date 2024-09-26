import { Component } from '@angular/core';
import { FormControl, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { PostPokemon } from '../../interfaces/base-pokemon';
import { PokeapiService } from '../../services/pokeapi.service';

@Component({
  selector: 'app-pokemon-form',
  standalone: true,
  imports: [ReactiveFormsModule],
  templateUrl: './pokemon-form.component.html'
})
export class PokemonFormComponent {

  pokemonForm: FormGroup = new FormGroup({
    name: new FormControl<string>('', Validators.required),
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
  });

  constructor(
    private pokemonService: PokeapiService
  ) {}

  createPokemon() {
    if (this.pokemonForm.status == 'VALID') {

      const newPokemon: PostPokemon = {
        name: this.pokemonForm.value.name,
        height: this.pokemonForm.value.height,
        weight: this.pokemonForm.value.weight,
        hp: this.pokemonForm.value.hp,
        attack: this.pokemonForm.value.attack,
        defense: this.pokemonForm.value.defense,
        specialAttack: this.pokemonForm.value.specialAttack,
        specialDefense: this.pokemonForm.value.specialDefense,
        speed: this.pokemonForm.value.speed,
        spriteFrontDefault: this.pokemonForm.value.spriteFrontDefault,
        spriteFrontShiny: this.pokemonForm.value.spriteFrontShiny
      }
      this.pokemonService.postPokemon(newPokemon).subscribe({
        next: res => {
          this.pokemonForm.reset();
          alert('El pokemon ' + res.name + ' ha sido guardado con éxito');
        }, error: err => {
          console.log(err);
          alert("Credenciales incorrectas");
        }
      });
    } else {
      alert('Debe completar todos los campos obligatorios para crear un pokemon')
    }
  }

}
