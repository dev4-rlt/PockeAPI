import { Component, EventEmitter, Output } from '@angular/core';
import { PostMove } from '../../interfaces/post-pokemon-details';
import { FormControl, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';

@Component({
  selector: 'app-move-form',
  standalone: true,
  imports: [ReactiveFormsModule],
  templateUrl: './move-form.component.html'
})
export class MoveFormComponent {

  @Output() move = new EventEmitter<PostMove>();

  moveForm: FormGroup = new FormGroup({
    name: new FormControl<string>('', Validators.required),
    description: new FormControl<string>(''),
  });

  createMove() {
    this.move.emit(this.moveForm.value);
    this.moveForm.reset();
    alert('Movimiento añadido con éxito')
  }

}
