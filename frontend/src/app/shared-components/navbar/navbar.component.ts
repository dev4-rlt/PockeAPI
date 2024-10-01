import { Component } from '@angular/core';
import { Router, RouterLink } from '@angular/router';
import { StorageService } from '../../services/storage.service';
import { NgClass } from '@angular/common';

@Component({
  selector: 'app-navbar',
  standalone: true,
  imports: [RouterLink, NgClass],
  templateUrl: './navbar.component.html'
})
export class NavbarComponent {

  pokemonListDisabled: boolean = false;
  formsDisabled: boolean = false;

  constructor(
    private storageService: StorageService,
    public router: Router
  ) { }

  logout() {
    this.storageService.name = '';
    this.storageService.address = '';
    this.router.navigate(['/'])
  }

}
