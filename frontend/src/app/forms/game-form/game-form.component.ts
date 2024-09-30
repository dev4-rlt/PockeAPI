import { Component, EventEmitter, Input, Output } from '@angular/core';
import { GameForm } from '../../interfaces/post-pokemon-details';
import { FormGroup, FormControl, Validators, ReactiveFormsModule, FormArray } from '@angular/forms';

@Component({
  selector: 'app-game-form',
  standalone: true,
  imports: [ReactiveFormsModule],
  templateUrl: './game-form.component.html'
})
export class GameFormComponent {

  @Input({ required: true }) gameArray!: FormArray<FormGroup<GameForm>>;
  @Output() close = new EventEmitter();

  gameForm: FormGroup = new FormGroup({
    name: new FormControl<string>('', Validators.required)
  });

  createGame() {
    this.gameArray.push(this.gameForm);
    this.close.emit();
  }

}
