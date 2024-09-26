import { Component, OnInit } from '@angular/core';
import { ReactiveFormsModule, Validators, FormControl, FormGroup } from '@angular/forms';
import { UserService } from '../../services/user.service';
import { LoginUser } from '../../interfaces/base-user';
import { StorageService } from '../../services/storage.service';
import { Router, RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-login-form',
  standalone: true,
  imports: [ ReactiveFormsModule, RouterOutlet, RouterLink, RouterLinkActive ],
  templateUrl: './login-form.component.html'
})
export class LoginFormComponent implements OnInit {
  
  loginForm: FormGroup = new FormGroup({
    username: new FormControl<string>('', Validators.required),
    password: new FormControl<string>('', Validators.required),
  });

  constructor(
    private userService: UserService,
    private storageService: StorageService,
    private router: Router
  ) { }

  ngOnInit(): void {
    this.storageService.name = '';
    this.storageService.address = '';
  }

  onSubmit(){
    if (this.loginForm.status == 'VALID') {
      const credentials: LoginUser = {
        username: this.loginForm.value.username,
        password: this.loginForm.value.password
      }
      this.userService.login(credentials).subscribe({
        next: res => {
          this.storageService.name = res.name;
          this.storageService.address = res.address;
          this.router.navigate(['dashboard'])
        }, error: err => {
          console.log(err);
          alert("Credenciales incorrectas");
        }
      });
    } else {
      alert('Debe completar todos los campos para iniciar sesión')
    }
  }
}