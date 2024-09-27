import { Component, EventEmitter, Output } from '@angular/core';
import { PostGame } from '../../interfaces/post-pokemon-details';
import { FormGroup, FormControl, Validators, ReactiveFormsModule } from '@angular/forms';

@Component({
  selector: 'app-game-form',
  standalone: true,
  imports: [ReactiveFormsModule],
  templateUrl: './game-form.component.html'
})
export class GameFormComponent {

  @Output() game = new EventEmitter<PostGame>();

  gameForm: FormGroup = new FormGroup({
    name: new FormControl<string>('', Validators.required)
  });

  createGame() {
    this.game.emit(this.gameForm.value);
    this.gameForm.reset();
    alert('Juego añadido con éxito')
  }

}
