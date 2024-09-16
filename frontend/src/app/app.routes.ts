import { Routes } from '@angular/router';
import { MostradorComponent } from './mostrador/mostrador.component';
import { SaludoComponent } from './saludo/saludo.component';

export const routes: Routes = [
    { path: '', component: SaludoComponent },
    { path: 'mostrador', component: MostradorComponent }
];
