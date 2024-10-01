import { Component, Input } from '@angular/core';
import { Router, RouterLink } from '@angular/router';
import { StorageService } from '../../services/storage.service';

@Component({
  selector: 'app-navbar',
  standalone: true,
  imports: [RouterLink],
  templateUrl: './navbar.component.html'
})
export class NavbarComponent {

  @Input() home: boolean = true;
  @Input() pokemonList: boolean = true;
  @Input() forms: boolean = true;

  constructor(
    private storageService: StorageService,
    private router: Router
  ) { }

  logout() {
    this.storageService.name = '';
    this.storageService.address = '';
    this.router.navigate(['/'])
  }

}
