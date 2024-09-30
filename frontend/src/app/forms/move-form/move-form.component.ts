import { Component, EventEmitter, Input, Output } from '@angular/core';
import { MoveForm, PostMove } from '../../interfaces/post-pokemon-details';
import { FormArray, FormControl, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';

@Component({
  selector: 'app-move-form',
  standalone: true,
  imports: [ReactiveFormsModule],
  templateUrl: './move-form.component.html'
})
export class MoveFormComponent {

  @Input({ required: true }) moveArray!: FormArray<FormGroup<MoveForm>>;
  @Output() close = new EventEmitter();

  moveForm: FormGroup = new FormGroup({
    name: new FormControl<string | null>(null, Validators.required),
    description: new FormControl<string | null>(null),
  });

  createMove() {
    this.moveArray.push(this.moveForm);
    this.close.emit()
  }

}
