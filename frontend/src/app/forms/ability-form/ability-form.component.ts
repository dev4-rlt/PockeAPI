import { Component, EventEmitter, Output } from '@angular/core';
import { FormControl, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { PostAbility } from '../../interfaces/post-pokemon-details';

@Component({
  selector: 'app-ability-form',
  standalone: true,
  imports: [ReactiveFormsModule],
  templateUrl: './ability-form.component.html',
})
export class AbilityFormComponent {

  @Output() ability = new EventEmitter<PostAbility>();

  abilityForm: FormGroup = new FormGroup({
    name: new FormControl<string>('', Validators.required),
    description: new FormControl<string>(''),
  });

  createAbility() {
    this.ability.emit(this.abilityForm.value);
    this.abilityForm.reset();
    alert('Habilidad añadida con éxito')
  }

}
