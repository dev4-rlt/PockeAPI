import { Component, OnInit } from '@angular/core';
import { ReactiveFormsModule } from '@angular/forms';
import { LoginFormComponent } from "../forms/login-form/login-form.component";
import { NavbarComponent } from '../shared-components/navbar/navbar.component';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [ReactiveFormsModule, LoginFormComponent, NavbarComponent],
  templateUrl: './login.component.html'
})
export class LoginComponent implements OnInit {

  ngOnInit(): void {
    document.title = 'Inicio de Sesión';
  }

}