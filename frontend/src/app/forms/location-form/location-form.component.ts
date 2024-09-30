import { Component, EventEmitter, Input, Output } from '@angular/core';
import { FormGroup, FormControl, Validators, ReactiveFormsModule, FormArray } from '@angular/forms';
import { LocationForm, PostLocation } from '../../interfaces/post-pokemon-details';

@Component({
  selector: 'app-location-form',
  standalone: true,
  imports: [ReactiveFormsModule],
  templateUrl: './location-form.component.html'
})
export class LocationFormComponent {
  
  @Input({ required: true }) locationArray!: FormArray<FormGroup<LocationForm>>;
  @Output() close = new EventEmitter();

  locationForm: FormGroup = new FormGroup<LocationForm>({
    name: new FormControl<string | null>(null, Validators.required)
  });

  createLocation() {
    this.locationArray.push(this.locationForm)
    this.close.emit();
  }
}
