import { Component, OnInit } from '@angular/core';
import { ReactiveFormsModule } from '@angular/forms';
import { LoginFormComponent } from "../forms/login-form/login-form.component";

@Component({
  selector: 'app-reactive',
  standalone: true,
  imports: [ReactiveFormsModule, LoginFormComponent],
  templateUrl: './reactive.component.html'
})
export class ReactiveComponent implements OnInit {
  ngOnInit(): void {
    document.title = 'Inicio de Sesión';
  }
}