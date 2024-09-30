import { Component, EventEmitter, Input, Output } from '@angular/core';
import { FormArray, FormControl, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { AbilityForm, PostAbility } from '../../interfaces/post-pokemon-details';

@Component({
  selector: 'app-ability-form',
  standalone: true,
  imports: [ReactiveFormsModule],
  templateUrl: './ability-form.component.html',
})
export class AbilityFormComponent {

  @Input({ required: true }) abilityArray!: FormArray<FormGroup<AbilityForm>>;

  @Output() close = new EventEmitter();

  abilityForm: FormGroup = new FormGroup<AbilityForm>({
    name: new FormControl<string | null>(null, Validators.required),
    description: new FormControl<string | null>(null),
  });

  createAbility() {
    this.abilityArray.push(this.abilityForm);
    this.close.emit();
  }

}
