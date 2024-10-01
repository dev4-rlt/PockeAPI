import { Routes } from '@angular/router';
import { PrincipalComponent } from './principal/principal.component';
import { HomeComponent } from './home/home.component';
import { LoginComponent } from './login/login.component';
import { DashboardComponent } from './dashboard/dashboard.component';

export const routes: Routes = [
    { path: '', component: HomeComponent },
    { path: 'mostrador', component: PrincipalComponent },
    { path: 'login', component: LoginComponent },
    { path: 'dashboard', component: DashboardComponent }
];
