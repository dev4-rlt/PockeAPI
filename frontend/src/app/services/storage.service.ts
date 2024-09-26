import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class StorageService {

  name: string = '';
  address: string = '';

  constructor() { }
}
