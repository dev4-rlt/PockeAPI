import { Component, OnInit } from '@angular/core';
import { StorageService } from '../services/storage.service';
import { Router } from '@angular/router';
import { PokemonFormComponent } from '../forms/pokemon-form/pokemon-form.component';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [PokemonFormComponent],
  templateUrl: './dashboard.component.html'
})
export class DashboardComponent implements OnInit {
  name: string = '';
  address: string = '';

  constructor(
    private storageService: StorageService,
    private router: Router
  ) { }

  ngOnInit(): void {
    // if (this.storageService.name == '') {
    //   this.router.navigate(['login']);
    // }
    document.title = 'Dashboard';
    this.name = this.storageService.name;
    this.address = this.storageService.address;
  }
}
