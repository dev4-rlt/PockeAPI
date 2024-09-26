import { Routes } from '@angular/router';
import { MostradorComponent } from './mostrador/mostrador.component';
import { SaludoComponent } from './saludo/saludo.component';
import { ReactiveComponent } from './reactive/reactive.component';
import { DashboardComponent } from './dashboard/dashboard.component';

export const routes: Routes = [
    { path: '', component: SaludoComponent },
    { path: 'mostrador', component: MostradorComponent },
    { path: 'login', component: ReactiveComponent },
    { path: 'dashboard', component: DashboardComponent }
];
