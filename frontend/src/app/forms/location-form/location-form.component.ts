import { Component, EventEmitter, Output } from '@angular/core';
import { FormGroup, FormControl, Validators, ReactiveFormsModule } from '@angular/forms';
import { PostLocation } from '../../interfaces/post-pokemon-details';

@Component({
  selector: 'app-location-form',
  standalone: true,
  imports: [ReactiveFormsModule],
  templateUrl: './location-form.component.html'
})
export class LocationFormComponent {
  
  @Output() location = new EventEmitter<PostLocation>();

  locationForm: FormGroup = new FormGroup({
    name: new FormControl<string>('', Validators.required)
  });

  createLocation() {
    this.location.emit(this.locationForm.value);
    this.locationForm.reset();
    alert('Locación añadida con éxito')
  }
}
