import { Component } from '@angular/core';
import { RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router';
import { NavbarComponent } from './shared-components/navbar/navbar.component';
import { StorageService } from './services/storage.service';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, RouterLink, RouterLinkActive, NavbarComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  constructor(
    private storageSvc: StorageService
  ) { }

  get isLoged(): boolean {    
    if (this.storageSvc.name != null && this.storageSvc.name != '') {
      return true;
    }
    return false;
  }
}